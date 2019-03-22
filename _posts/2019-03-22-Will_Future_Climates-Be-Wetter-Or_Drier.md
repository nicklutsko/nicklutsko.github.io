---
layout: post
title: "Will Future Climates Be Wetter Or Drier?"
date: 2019-03-22
use_math: true
---

<p>One of the most important potential impacts of future climate change is on the water supply: will future climates be wetter or drier? Clearly, this has major implications for human life and for econsystems, and a particular worry is that warmer climates will experience more droughts $($or even <a href="https://en.wikipedia.org/wiki/Megadrought">mega droughts</a>$)$.</p>

<p>It turns out that the answer depends on what we mean by "wetter" and "drier". For instance, one way to quantify these is with indices which measure the severity of droughts or which give some more general measure of how "arid" $($dry and dusty$)$ a climate is. Two commonly used indices are the Palmer Drought Severity Index $($PDSI$)$ and the ratio of precipitation $($P$)$ to "potential evapotranspiration" $($<a href="https://en.wikipedia.org/wiki/Potential_evaporation">PET</a>$)$. We can also measure water availability and its impacts directly, through things like precipitation minus evaporation $($P-E, equal to the river runoff$)$ and net primary productivity $($NPP$)$. These correspond more closely to what we actually care about: river levels and plant growth.</p>

<p>Climate models give different answers depending on whether we use indices or direct measurements. Models robustly project "drier" future climates, in the sense of larger PDSI and smaller P/PET ratios. Going the other way, to cooler climates, they also suggest that the Last Glacial Maximum $($LGM – hopefully the last acronym$)$ was wetter than today – PDSI was lower and P/PEI was higher. But P-E is more ambiguous, and NPP is projected to increase in future climates and likely decreased in colder climates. <a href="https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-16-0854.1">Scheff et al. $($2017$)$</a> did a very thorough analysis of these, and you can see the differences between indices and direct measurements for model simulations of future warming:</p>

<img src="http://nicklutsko.github.io/notes/images/Scheff_rcp_proj.png" alt="RCP85 projections" style="position:absolute; left:150px; width:672px;height:603px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>and simulations of the LGM:</p> 

<img src="http://nicklutsko.github.io/notes/images/Scheff_LGM.png" alt="LGM simulations" style="position:absolute; left:150px; width:657px;height:591px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>There are several reasons why the indices predict drying at warmer temperatures. First, they have drying "baked in" to them: warmer, sunny conditions tend to enhance evaporation, making things look more arid. It seems like the indices are too sensitive to temperature $($or at least to temperature changes$)$, and taking out this temperature dependence makes the wetting/drying signals weaker $($<a href="https://www.nature.com/articles/nclimate3046">Milly and Dunne, 2016</a>, see also <a href="https://pages.uncc.edu/hcl/wp-content/uploads/sites/1187/2018/08/Scheff-2018-Indices-Impacts.pdf">this review</a>$)$.</p> 

<p>Another factor is that we expect relative humidity to decrease over land. All else equal, lower relative humidities results in more evaporation, making land drier. <a href="http://www.mit.edu/~pog/src/byrne_land_relative_humidity_decrease_2016.pdf">Byrne and O'Gorman (2016)</a> give a simple explanation for this reduction in relative humidity: suppose the specific humidity is set by the specific humidity over the ocean $($where most evaporation happens$)$. Relative humidity over land is then proportional to the relative humidity over  ocean times the ratio of land temperature to ocean temperature:
$$
RH_{land} = \gamma RH_{ocean} \times T_{ocean} / T_{land},
$$
where $\gamma$ is a constant of proportionality. Assuming the changes in $RH_{ocean}$ and $\gamma$ are negligible, the change in $RH_{land}$ comes from the ratio of ocean warming to land warming. Since we also expect land to warm more than the ocean surface $($<a href="https://journals.ametsoc.org/doi/10.1175/JCLI-D-12-00262.1">Byrne and O’Gorman</a> again$)$, this ratio decreases, and $RH_{land}$ decreases.</p>

<p>Finally, the indices don’t seem to account for the effects of warming, and higher CO2 levels, on plants. At higher CO2 levels plants’ stomatal conductance decreases -- they lose less water to the atmosphere – and so plants retain more water, making the overall land surface moister. Plants are also “fertilized” by higher CO2 concentrations: they need CO2 to grow, so higher CO2 levels encourage more plant growth $($An important caveat is that these effects vary by plant-type, and plant growth can also be limited by other nutrients, like iron$)$.</p>

<p>This also effects the runoff, P - E. As you can see from the figures, there are regions of drying, like the Amazon and in the subtropics/mid-latitudes, and moistening, like over equatorial Africa and at high latitudes. Part of this response comes from changes in plants, but we can also understand them physically.</p>

<p>Changes in P – E can be divided into a thermodynamic component $($changes in how much water the atmosphere holds$)$ and a dynamic component $($changes in circulation patterns$)$. We expect the deep tropics on the whole to get moister, because of the thermodynamic effect: warm air holds more water vapor. But circulation changes can be important on a regional level. For instance, Figure 9 of <a href="https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-12-00543.1">Chadwick et al. (2013)</a> suggests that the drying over the Amazon comes from shifts in deep convection, with this being reduced over the Amazon. I haven’t found more about this, but it seems worth understanding better. The convection over equatorial Africa doesn’t change as much, so the thermodynamic effect dominates there and P – E increases. </p> 

<p>The drying of the subtropics/mid-latitudes comes partially from a thermodynamic effect – these regions are already dry, and so they dry further in a warmer climate – and partly because transient eddies carry more water to higher latitudes, causing the enhanced P - E at high latitudes $($see Figure 13 of <a href="https://journals.ametsoc.org/doi/pdf/10.1175/2010JCLI3655.1">Seager et al, 2010</a>$)$.</p> 

<p>Despite these issues with the indices, an important process they may be relevant for is fires. These tend to occur for warm, dry conditions – the kinds of conditions quantified by PDSI and P/PET. Past fire rates are hard to measure, but there’s some evidence that there were fewer fires during the LGM than during the pre-industrial period – agreeing with the intuition from the indices that the LGM was wetter than today.</p> 

<p>I also wonder whether the NPP and P-E changes in the figures above are somewhat misleading, because these are absolute changes, not relative changes. In regions with little vegetation $($the Sahara, the Kalahari, etc.$)$, where plants also don’t buffer the water supply, there may be more of a drying signal. But these regions have very small NPP and P-E, so these changes don’t pop out so much. It would be particularly interesting to focus in on the borders of deserts – this is where desertification is and will happen. For instance, there are some physical arguments for why the Sahel will become drier in a warmer world $($see <a href="https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-18-0238.1">here</a>$)$.</p>

<p>In any case, future changes in water availability are much more ambiguous than changes in temperatures, and the projected changes are sensitive to how water availability is measured. The results summarized here are also at the resolution of climate models, but water is something we care about on a local level. At smaller scales, too fine to be resolved by climate models, things might be quite different from the broad-brush pictures suggests by climate models.</p>






