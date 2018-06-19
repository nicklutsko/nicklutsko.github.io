---
layout: post
title: "Decision-Making and Subjective Uncertainty: Using Integrated Assessment Models to Inform Climate Policy"
date: 2018-06-19
---

<p markdown="1"><a href="https://en.wikipedia.org/wiki/Integrated_assessment_modelling">Integrated Assessment Models (IAMs)</a> are one of the main tools used by policy makers to predict the economic impacts of climate change. For instance, they played an important role in determining the Paris Climate Goals, and are used by the US government to estimate the “social cost” of carbon (SCC). It’s worrying then that they’ve been criticized recently for drastically underestimating the potential risks of global warming (see <a href="https://www.vox.com/energy-and-environment/2018/6/8/17437104/climate-change-global-warming-models-risks">David Roberts’ article on Vox</a> for a summary)</p>

<p>The technical reasons for the shortcomings of IAMs can get involved, but some of the critiques raise an interesting question that is more fundamental to thinking about climate policy: how can we make decisions in the face of large uncertainties? And not just large uncertainties, but what are sometimes called “subjective” uncertainties?</p>

<h3>What Are IAMs?</h3>

<p>IAMs are made up of a simplified model of the carbon-climate system coupled to a “general equilibrium” economic model:</p>

<center><img src="http://nicklutsko.github.io/notes/images/IAMs.png" alt="IAMs" style="width:320px;height:234px;" class="center"></center>

<p>The economic model predicts carbon emissions, which are fed to the carbon-climate model, and the climate model estimates a “damage function”, which is given back to the economic model. Together, these can be used to explore the economic impacts of socio-economic storylines. For instance, we could compare a “business-as-usual” storyline with a future in which there is aggressive mitigation, and see which scenario would result in the higher overall economic growth.</p>

<p>IAMs combine models for two systems we can’t model very well: the climate system and (even worse) the economy; so their results have a lot of uncertainty, and they’ve been described as <a href="http://www.nber.org/papers/w19244">"close to useless as tools for policy analysis"</a>. But they’re still the best tool we have for predicting the potential economic impacts of climate change, and they actively inform policy decisions, so it’s important that we make them as good as we can.</p>

<h3>Subjective Uncertainty</h3>

<p>We can divide up the sources of uncertainty in IAMs into “objective” uncertainties and “subjective” uncertainties. On the climate side, climate sensitivity  – how much the Earth will warm up for an increase in CO<sub>2</sub> concentrations – is an objective uncertainty. We can run experiments with a set of climate models and then use the distribution of their sensitivities to get a best estimate of Earth’s climate sensitivity and also to put error bars on this estimate. The only places where human judgment comes in are in whether to exclude bad models  and in how to calculate the error bars.</p>

<p>An example of a subjective uncertainty is the question of how close we are to any <a href="https://www.annualreviews.org/doi/10.1146/annurev-environ-102511-084654">“tipping points”</a>. For instance, global warming <a href="http://blogs.ei.columbia.edu/2017/06/06/could-climate-change-shut-down-the-gulf-stream/">could cause the meridional overturning circulation in the ocean to suddenly shut off</a>, which would be a disaster for society. But we don’t have a precise idea how close we are to this actually happening, whether it would take 2 degrees of warming or 8 degrees. This isn’t the only tipping point that we know of, and the others are all similarly unconstrained</p>

<p>Another way to put this is that our estimates of the tail risks of climate change are basically educated guesses.</p>

<p>Things get even worse on the economic side. An important subjective uncertainty is the discount rate: how much we want to push the costs of climate change onto future generations. Taking a steep discount rate means that we expect future generations to come up with technological innovations to deal with the effects of climate change and so we shouldn’t worry about emitting carbon today. A low discount rate leads to the opposite conclusion, and says that we should be doing everything we can to reduce carbon emissions. </p>

<p>This isn’t something with a “correct” answer, but it has a huge impact on projections of climate change impacts. <a href="http://www.nber.org/papers/w19244">Pindyck (2017)</a> suggests that much of the difference between Nordhaus (2008)’s estimate of $20/ton for the SCC and Stern (2008)’s estimate of $200/ton comes from differences in their assumptions about the discount rate.</p>

<p>The general issue of subjective uncertainty is also referred to as the issue of having multiple priors (really multiple non-overlapping priors):</p>

<center><img src="http://nicklutsko.github.io/notes/images/multiple_priors.png" alt="Multiple Priors" style="width:526px;height:288px;" class="center"></center>

<p>Multiple priors are likely to come up whenever an uncertainty is poorly constrained and so people’s opinions and biases come into play when quantifying the uncertainty.</p>

<h3>Uncertainty in IAMs</h3>

<p>How do IAMs deal withs subjective uncertainty? Basically by ignoring it.  IAMS use “expected utility functions” to integrate over their uncertainties, but the utility functions are based on the judgments of the people building them, and so they only consider a single prior (this is why the estimates of the SCC by Nordhaus and by Stern can be so different).</p>

<p>They also ignore the tail risks on the climate side, so that even large warmings have relatively small economic impacts. The thinking seems to be that since we don’t know how close we are to any tipping points, IAMs shouldn’t take them into account. And it’s actually worse than that, since they also omit the effects of climate changes that are hard to quantify economically, like ocean acidification. (More <a href="https://academic.oup.com/reep/advance-article/doi/10.1093/reep/rey005/5025082">here</a>).</p>

<p>So IAMs both underestimate the risks of climate change and the uncertainty of their predictions. This is doesn’t seem like an ideal situation.</p>

<h3>How Can We Account for Subjective Uncertainty?</h3>

<p>There has been some recent theoretical work on how to extend the expected utility framework to include multiple priors (see <a href="https://www0.gsb.columbia.edu/faculty/gheal/EnvironmentalEconomicsPapers/REEP%20uncertainty%20published.pdf">here</a> and <a href="http://personal.lse.ac.uk/MILLNER/files/handbook.pdf">here</a>). The simplest way is to replace the expected utility functions with “max-min” expected utility. This means that we compare policies based on their worst-case outcome, considering all of the priors.</p>

<p>This can be made more elaborate. For instance, we could combine the best and worst outcomes of each policy (e.g., 0.6 times the worst outcome + 0.4 times the best outcome) or weight the outcomes by our (subjective) estimate of how likely each one is.</p>

<p>Whatever choice we make involves ethical decisions. The max-min approach is the most risk-averse method of evaluating policy choices, and speaks to the preference people have for <a href="https://en.wikipedia.org/wiki/Ambiguity_aversion">“ambiguity aversion”</a> (“better the devil you know than the devil you don’t”). So if they felt like there was a non-negligible change of disastrous climate change (say 5%), then people would generally prefer to take the certain cost of paying today over the uncertain cost of betting on the potential of disaster.</p>

<p>The opposite would be a “max-max” approach, which would take the best possible outcome of each policy, and would be a heavy bet against climate change having major impacts.
</p>

<p>Because IAMs currently ignore tail risks and subjective uncertainty, pretty much whatever we do to incorporate these into IAM studies will increase how much damage we expect climate change to have. So adding these into our decision making is pretty urgent. I’m not sure what the best way of doing this is (max-min does seem a bit too cautious), but it’s clear we can’t just ask “what impacts could this policy have” and have to include a preference for how risk adverse we are, or else who’s (subjective) opinions we trust the most. </p>

<p>Perhaps the most important thing is that however uncertainties are accounted for, this choice must be clearly communicated to policy makers. If the result of a max-min study suggests we should be urgently reducing CO<sub>2</sub> emissions, the people making decisions should be clear that this is based on a conservative comparison of worst-case scenarios. It might even be better to take this further and have policy makers choose how to balance risk-aversion with subjective estimates of uncertainty in making projections of future climate scenarios. Since they are the ones who will make the decisions, they should be involved in modeling the potential impacts of these decisions. </p>



