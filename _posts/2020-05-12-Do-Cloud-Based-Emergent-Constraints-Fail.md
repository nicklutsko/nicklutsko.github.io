---
layout: post
title: "Do Cloud-Based Emergent Constraints on Climate Sensitivity Fail in CMIP6?"
date: 2020-05-12
---

In a <a href="https://nicklutsko.github.io/blog/2020/02/02/Historical-Warming-Climate-Sensitivity">previous post</a>, I described two classes of emergent constraints on climate sensitivity: temperature-based constraints and cloud-based constraints. Temperature-based emergent constraints compare warming rates in historical simulations with observed temperature trends, and rule out models which don’t reproduce the observed record well. Cloud-based emergent constraints look at relationships between cloud cover (or cloud radiative effects) and surface temperatures on monthly, annual, etc. time-scales, and correlate these relationships across models with climate sensitivity. The idea is that since most of the uncertainty in climate sensitivity comes from clouds, the response of clouds to internal variability should tell us something about how clouds respond to warming.

<p>A cloud-based emergent constraint that I've played around with is a "regional" constraint, in which net or SW CRE and surface temperatures are binned into 5&#176; by 5&#176; boxes (the size of the boxes doesn't really matter) and local regression co-efficients (\(\alpha_{loc}\)) are calculated. That is, for a box \(i/), (\(\alpha_{i} = \delta net CRE / \delta T_s\)). These local regression co-efficients, for each box, can then be correlated across models with the models' (global) climate sensitivities.</p>

I like this approach for several reasons: it hones in on the most relevant regions for developing emergent constraints, and if there are multiple "hot-spot" regions then the climate sensitivity estimates produced by each region can be checked against the others, providing a consistency check. It would be exciting if distinct climate regimes, like the subtropical north Pacific and the Southern Ocean, gave similar estimates of ECS. 

<p>In CMIP5 this regional constraint works well, consistent with other cloud-based emergent constraints. The figure below shows \(r^2\) values for correlations across models between  \(\alpha_{loc}\) and equilibrium climate sensitivity (ECS) for 18 CMIP5 models. The \(\alpha_{loc}\) values are estimated from historical simulations, and the top panel shows results using monthly data and the bottom panel shows results using annual-mean data.</p> 
<img src="http://nicklutsko.github.io/notes/images/Box_plots_CRE_r2.png" alt="CMIP5 regional" style="position:absolute; left:180px; width:600px;height:500px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

A number of "hot-spots" show-up, mostly on the edge of subtropical stratocumulus regions, with the most prominent  in the northeast Pacific, roughly over Hawaii. Combining surface temperatures from the ERA-Interim reanalysis and net CRE data from CERES, I have a rough emergent constraint on ECS based on the average value of monthly \(\alpha_{loc}\) in the region outlined by the red box.

<img src="http://nicklutsko.github.io/notes/images/CMIP5_emergent_constraint.png" alt="CMIP5 emergent constraint" style="position:absolute; left:280px; width:400px;height:300px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

This seems promising, but one of the criteria <a href="https://journals.ametsoc.org/doi/10.1175/JCLI-D-17-0631.1">Caldwell et al.</a> use to define a "credible" emergent constraint is that it holds in multiple ensembles. So how does the regional emergent constraint do in CMIP6? Not well...

<img src="http://nicklutsko.github.io/notes/images/CMIP6_Box_plots_CRE_r2.png" alt="CMIP6 regional" style="position:absolute; left:180px; width:600px;height:500px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

Why wouldn’t cloud-based emergent constraints work in CMIP6? <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019GL085782">Zelinka et al.</a> showed that (in the ensemble-mean) the high ECS values in CMIP6 are mostly due to large cloud feedbacks over the Southern Ocean. Whereas in CMIP5 (and also in CMIP3), most of the uncertainty in the cloud feedback came from subtropical descent regions. So one guess is that CMIP6 has something like three classes of models: low sensitivity models, high sensitivity models driven by Southern Ocean cloud feedbacks and high sensitivity models driven by subtropical clouds (see also <a href="https://twitter.com/mzelinka/status/1256008091029499904">this plot</a> Mark posted on Twitter). Emergent constraints based on the variability of clouds in regions of subtropical descent would then fail, as would constraints based on Southern Ocean clouds. The only hope for a cloud-based emergent constraint would be if there were correlations between southern ocean clouds and subtropical clouds, or if we could rule out one group of high sensitivity models.

I don't think this means the cloud-based emergent constraints that worked in CMIP5 are wrong, necessarily, but it does seem like it might be harder to develop this kind of emergent constraint for the CMIP6 models.

(Thanks to Joel Norris and Cristi Proistosescu for helpful conversations.)




