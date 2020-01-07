var smartquotes = require('smartquotes');

var _require = require('idyll-ast/v1'),
    modifyNodesByName = _require.modifyNodesByName,
    modifyChildren = _require.modifyChildren,
    getNodesByName = _require.getNodesByName,
    prependNodes = _require.prependNodes,
    removeNodesByName = _require.removeNodesByName,
    removeProperty = _require.removeProperty,
    setProperty = _require.setProperty,
    getProperty = _require.getProperty,
    getNodeName = _require.getNodeName,
    createTextNode = _require.createTextNode,
    createNode = _require.createNode;

var attrConvert = function attrConvert(list) {
  return (list || []).reduce(function (acc, _ref) {
    var name = _ref[0],
        _ref$ = _ref[1],
        type = _ref$[0],
        val = _ref$[1];

    if (type === 'value') {
      acc[name] = val;
    }
    return acc;
  }, {});
};

var cleanResults = function cleanResults(ast, options) {
  if (typeof ast === 'string') {
    if (options.smartquotes) {
      return smartquotes(ast);
    }
    return ast;
  }

  return ast.map(function (node) {
    if (typeof node === 'string') {
      if (options.smartquotes) {
        return smartquotes(node);
      }
      return node;
    }

    node[2] = flattenChildren(node[2]);

    var name = node[0].toLowerCase();
    var rawNodes = ['pre', 'code', 'codehighlight', 'equation'];
    if (['section', 'step', 'textcontainer'].indexOf(name) === -1 && node[2].length === 1 && typeof node[2][0] !== 'string' && node[2][0][0] === 'p' && node[2][0][2]) {
      if (rawNodes.indexOf(name) > -1) {
        return [node[0], node[1], node[2][0][2]];
      }
      return [node[0], node[1], cleanResults(node[2][0][2], options)];
    }

    // don't apply cleaning to codeblocks
    if (rawNodes.indexOf(name) > -1) {
      return node;
    }
    return [node[0], node[1], cleanResults(node[2], options)];
  });
};

var flattenChildren = function flattenChildren(ast) {
  return (ast || []).reduce(function (acc, child) {
    if (child[0] === '_idyllContainer') {
      acc = acc.concat(child[2]);
    } else {
      acc.push(child);
    }
    return acc;
  }, []);
};

var makeFullWidth = function makeFullWidth(ast) {
  var currentTextContainer = [];
  var reduced = (ast || []).reduce(function (acc, child) {
    if (typeof child === 'string') {
      currentTextContainer.push(child);
      return acc;
    }
    var attrs = attrConvert(child[1] || []);
    var childName = child[0].toLowerCase();
    if (['derived', 'var', 'data', 'fullwidth', 'scroller'].indexOf(childName) > -1 || attrs.fullWidth) {
      if (childName === 'fullwidth') {
        child[0] = 'div';
        var className = getProperty(child, 'className');
        if (className) {
          switch (className[0]) {
            case 'value':
              child = setProperty(child, 'className', ['value', 'fullWidth ' + className[1]]);
              break;
            case 'expression':
              child = setProperty(child, 'className', ['expression', '"fullWidth " + (' + className[1] + ')']);
              break;
            case 'variable':
              child = setProperty(child, 'className', ['expression', '"fullWidth " + (' + className[1] + ')']);
              break;
            default:
              child = setProperty(child, 'className', ['value', 'fullWidth']);
          }
        } else {
          child = setProperty(child, 'className', ['value', 'fullWidth']);
        }
      } else {
        child = removeProperty(child, 'fullWidth');
      }

      if (currentTextContainer.length) {
        acc = acc.concat([['TextContainer', [], currentTextContainer], child]);
      } else {
        acc = acc.concat([child]);
      }
      currentTextContainer = [];
    } else {
      currentTextContainer.push(child);
    }
    return acc;
  }, []);

  if (currentTextContainer.length) {
    return reduced.concat([['TextContainer', [], currentTextContainer]]);
  }
  return reduced;
};

var hoistVariables = function hoistVariables(ast) {
  var vars = getNodesByName(ast, 'var');
  var derived = getNodesByName(ast, 'derived');
  var data = getNodesByName(ast, 'data');

  ast = removeNodesByName(ast, 'var');
  ast = removeNodesByName(ast, 'derived');
  ast = removeNodesByName(ast, 'data');

  ast = prependNodes(ast, derived);
  ast = prependNodes(ast, data);
  ast = prependNodes(ast, vars);

  return ast;
};

var wrapText = function wrapText(ast) {
  return modifyNodesByName(ast, 'TextContainer', function (node) {
    return modifyChildren(node, function (child) {
      if (typeof child === 'string') {
        return ['p', [], [child]];
      }
      return child;
    });
  });
};

/**
 * Plugin to find find valid urls in text nodes and make them hyperlinks.
 * @param {*} ast     AST passes from the parser representing the document.
 * @return A new modified AST with all hyperlinks linkified.
 */
var autoLinkify = function autoLinkify(ast) {
  return (ast || []).map(autoLinkifyHelper);
};

/**
 * Helper function for autoLinkify to check the type of node and modify them if necessary.
 * @param {*} node    node to be checked and modified if necessary.
 * @return modified node, if modification was required, else returns node.
 */
function autoLinkifyHelper(node) {
  if (typeof node === 'string') {
    return hyperLinkifiedVersion(node);
  } else if (['a', 'code', 'pre', 'equation'].indexOf(getNodeName(node).toLowerCase()) > -1) {
    return node;
  } else {
    return modifyChildren(node, autoLinkifyHelper);
  }
}

/**
 * Helper function for autoLinkifyHelper that modfies the text node if any hyperlinks are present.
 * @param {*} node
 * @return a modified node if any hyperlinks are present in the node, else returns node
 */
function hyperLinkifiedVersion(node) {
  var hyperLinks = getHyperLinksFromText(node);
  if (hyperLinks) {
    return seperateTextAndHyperLink(node, hyperLinks);
  } else {
    return node;
  }
}

/**
 * Helper function that seperates hyperlinks from textnodes
 * @param {*} textnode
 * @param {*} hyperlinks  Hyperlink array that has all the hyperlinks occuring in the textnode in order of appearance.
 * @return a new span element encampassing all the new textnodes and anchor tag.
 */
function seperateTextAndHyperLink(textnode, hyperlinks) {
  var match = void 0;
  var hyperLinkIndex = 0;
  var substringIndex = 0;
  var newChildNodes = [];
  while (hyperLinkIndex < hyperlinks.length) {
    var regexURL = new RegExp(hyperlinks[hyperLinkIndex], 'g');
    match = regexURL.exec(textnode.substring(substringIndex));
    if (match) {
      var linkEndIndex = regexURL.lastIndex;
      var linkStartIndex = linkEndIndex - hyperlinks[hyperLinkIndex].length;
      var textNodeValue = textnode.substring(substringIndex, linkStartIndex);
      if (textNodeValue !== '') {
        newChildNodes.push(createTextNode(textnode.substring(substringIndex, linkStartIndex)));
      }
      var anchorElement = createNode('a', [], [hyperlinks[hyperLinkIndex]]);
      setProperty(anchorElement, 'href', hyperlinks[hyperLinkIndex]);
      newChildNodes.push(anchorElement);
      textnode = textnode.substring(linkEndIndex);
      substringIndex = 0;
    }
    hyperLinkIndex++;
  }
  if (textnode != '') {
    newChildNodes.push(createTextNode(textnode));
  }
  return createNode('span', [], newChildNodes);
}

/**
 * This function returns an array with any hyperlinks in the passed textNode.
 * @param {*} textNode the text node to be tested for hyperlinks
 * @return List of URL's from the textNode
 */
function getHyperLinksFromText(textNode) {
  //Regular experession for matching URLs
  var regexURL = /(http|https|ftp|ftps)\:\/\/([a-zA-Z0-9\-\.]+\.)+[a-zA-Z]{2,3}(\/\S*)?/g;
  return textNode.match(regexURL);
}

module.exports = {
  cleanResults: cleanResults,
  flattenChildren: flattenChildren,
  hoistVariables: hoistVariables,
  makeFullWidth: makeFullWidth,
  wrapText: wrapText,
  autoLinkify: autoLinkify,
  autoLinkifyHelper: autoLinkifyHelper,
  hyperLinkifiedVersion: hyperLinkifiedVersion,
  seperateTextAndHyperLink: seperateTextAndHyperLink,
  getHyperLinksFromText: getHyperLinksFromText
};