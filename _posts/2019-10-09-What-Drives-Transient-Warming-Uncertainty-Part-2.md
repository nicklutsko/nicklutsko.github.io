---
layout: post
title: "What Drives Uncertainty in Transient Warming? Part 2 - Details"
date: 2019-10-09
---

<p>This is a follow-up to my post <a href="https://github.com/nicklutsko/TCR_Uncertainty/blob/master/TCR_Uncertainty.ipynb">"What Drives Uncertainty in Transient Warming?"</a>, which summarized a recent paper with Max Popp on <a href="https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GL084018">"Probing the Sources of Uncertainty in Transient Warming on Different Time Scales"</a>. Here I’m going to provide some of the details of the analysis.</p>

<p>A Jupyter notebook with our analysis is available <a href="https://github.com/nicklutsko/TCR_Uncertainty/blob/master/TCR_Uncertainty.ipynb">here</a>.</p>

<h3>Theory</h3>

<p>To understand the sensitivities of transient warming we started by analyzing the two box model. This can be solved for \(T_1\), either in real space or (more simply) by transforming to frequency space to give::
$$
\hat{T_1} = \frac{\omega}{70} \times \frac{F}{\lambda  + ic\omega +\epsilon\gamma \left(1 - \gamma /(ic_0\omega + \gamma)\right)},
$$
where we assume CO\(_2\) concentrations are going up by 1% per year. Looking at this expression gives a first sense for why the forcing matters so much: it’s the only term in the numerator, whereas there are several terms in the denominator. So even if the climate feedback (\(\lambda\)) was zero, the transient warming would still be finite (but the ECS would be infinite)..</p>

<p>We then calculated the absolute value of \(\hat{T_1}\), which is a complicated expression, but can be simplified into four transient warming regimes: 
<ul>
<li>the ultra-fast regime (\(t \(<\) t_H = \epsilon/(\lambda + \epsilon\gamma)\) ),</li>
<li>the fast regime (\(t_H \(<\) t \(<<\) t_L= c_0 /\gamma\) ),</li>
<li>the intermediate regime (\(t \leq t_L\) ),</li>
<li>the slow regime (\(t_L > t\)).</li>
</ul>
</p>

<p>Using ensemble-mean values from CMIP5, the fast time-scale \(t_H  \approx\) 4 years and the slow time-scale \(t_L \approx\) 160 years. The fast and intermediate regimes are separated by the time it takes for the deep ocean to warm up significantly – when \(T_2\) is meaningfully greater than 0. Defining this as the time when \(t = 0.1 c_0 / \gamma\) gives a time-scale of 16 years.</p>

<p>Our main goal was to separate out (1) the uncertainty in each variable, from (2) the sensitivity of transient warming to uncertainty in each variable. A variable could be highly uncertain but contribute little to uncertainty in the TCR, or vice-versa: a variable could be well known, but still be responsible for a lot of uncertainty. To put it another way: there’s a lot of emphasis on constraining the net feedback, but maybe there’s a better way of reducing uncertainty in the TCR?</p>

<p>Going through the different regimes: In the ultra-fast regime most of the uncertainty comes from the upper-ocean heat capacity \(c\). Basically, how quickly does the surface start warming up? If \(c\) is large then the warming in the first few years will be small, and vice-versa.</p>

<p>In the fast regime the forcing is responsible for most of the uncertainty, with \(\lambda\), \(\gamma\) and \(\epsilon\) also contributing. But because these are all in the denominator, their uncertainties cancel out somewhat, and \(F\) is the leading source of uncertainty. On these time-scales \(c\) is small compared to  \(λ + \epsilon \gamma\), so we don’t have to worry about the upper ocean heat capacity anymore.</p>

<p>Once the deep ocean has started warming, the ocean heat uptake parameters \(\gamma\) and \(\epsilon\) contribute less to uncertainty. You can see in the denominator of the equation that the term in brackets starts decreasing as \(c_0 \omega\) increases, and the effects of \(\gamma\) and \(\epsilon\) are muted. Physically, heat is transferred to the deep ocean through the term \(H = \epsilon\gamma(T_1 – T_2)\). \(H\) cools the upper layer (the surface), and so \(\gamma\) and \(\epsilon\) damp transient warming. But as the two layers come into equilibrium \(T_1 – T_2\) becomes small, so \(H\) is also small, and \(\gamma\) and \(\epsilon\) matter less. In equilibrium \(H\) is zero, and the values of \(\gamma\) and \(\epsilon\) don’t matter.</p>

<p>An interesting subtlety is that \(\gamma\) cools the surface layer directly, but also warms it indirectly by making \(T_2\) larger (and hence \(H\), which cools \(T_1\), smaller). These opposing direct and indirect effects on surface temperature mean that \(\gamma\) is responsible for less uncertainty than \(\epsilon\), which always damps surface temperature. (Note: one of the original motivations for our study was trying to clarify how the ocean contributes to transient warming uncertainty.)</p>

<p>Finally on long time-scales the two layers are in equilibrium with each other and we’re basically left with the ECS expression \(F / \lambda\), and the forcing and the feedback matter roughly equally.</p>

<p>So we can expect transient warming’s sensitivity to evolve as follows: 
<ul>
<li>for the first few years the upper ocean heat capacity matters most, but the importance of this quickly decreases,</li>
<li>then the warming is most sensitive to the forcing, with the feedback and the ocean heat uptake terms (\(\gamma\) and \(\epsilon\)) also contributing,</li>
<li>once the deep ocean has started heating up the sensitivity to the ocean heat uptake terms decreases, with the importance of \(\gamma\) decreasing faster than \(\epsilon\).</li>
</ul>
Through all, the importance of the feedback \(\lambda\) relative to the forcing slowly increases, so that on the longest timescales transient warming is roughly as sensitive to \(\lambda\) as to \(F\).
</p>


<h3>CMIP5 data</h3>

<p>To quantify things with some data, we fit the two box model to 1%/year simulations with a set of CMIP5 models. This gave the relative uncertainties in panel a of the figure below, where "relative uncertainty" is the standard deviation across the ensemble of a variable divided by the mean of the variable. Again, \(\lambda\) is about three times as uncertain as \(\F\), though the most uncertain variable is actually \(\c_0\).</p>

<p>To understand the contributions of each variable to uncertainty in the TCR, we then ran the two box model using the mean values of all the variables, except for one variable which we varied by \(\pm\) 2 standard deviations. E.g., we ran the model with \(F\), \(\lambda\), \(c\), \(c_0\) and \(\gamma\) set to their ensemble-mean values, but set \(\epsilon\) to one standard deviation above its ensemble-mean. This gave the TCR estimates shown in the box-and-whisker plots of panel b. The largest spread comes when \(\lambda\) is varied, and then when \(F\) is varied. \(\gamma\) and \(\epsilon\) are similar to each other, and the heat capacities are negligible.</p> 

<img src="http://nicklutsko.github.io/notes/images/eps_TCR_uncertainty_comp.png" alt="TCR uncertainty calculations" style="position:absolute; left:100px; width:648px;height:432px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>But this mixes the two aspects of uncertainty: the uncertainty in each variable, and the TCR’s sensitivity to that uncertainty. \(\lambda\) contributes the most to uncertainty, but it is also one of the most uncertain parameters. So we re-did the calculations but set the relative uncertainties for all variables to \(\lambda\)’s relative uncertainty (about 30%). These calculations (panel c) showed that the TCR is about twice as sensitive to uncertainty in the forcing than to uncertainty in the feedbacks, and from this we estimated that if the forcing was as uncertain as the feedback our best guess for the TCR would be \(\sim\)0.5-3.5\(^\circ\)C, instead of the actual range of 1-2.5\(^\circ\)C.</p> 

<p>We looked at the effects on different time-scales by calculating the ratio \(r\) of the sensitivity of transient warming to uncertainty in each variable divided by the sensitivity of transient warming in the forcing \(F\). So if \(r_\gamma > 1\) at \(t =\) 20 years, it means that warming after 20 years of increasing CO\(_2\) by 1%/year is more sensitivity to uncertainty in \(\gamma\) than uncertainty in \(F\). If \(r_\gamma \(<\) 1\), then the warming is more sensitive to \(F\) than to \(\gamma\).</p>

<img src="http://nicklutsko.github.io/notes/images/time_scale_uncertainty.jpg" alt="TCR uncertainty ratios" style="position:absolute; left:100px; width:576px;height:432px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>These calculations gave us exactly what we expected from the theory. Uncertainty in the upper ocean heat capacity matters a lot for the first few years, but quickly becomes negligible. The contributions of uncertainties in \(\gamma\) and \(\epsilon\) peak around 15 years, then diminish as the deep ocean heats up, with the contribution from \(\gamma\) decreasing faster than the contribution from \(\epsilon\). And the feedback \(\lambda\) becoming more important over time (though even after 140 years \(r_F\) is only \(\sim\)0.7.</p> 

<h3>Toy Calculations</h3>

<p>As mentioned in the previous post, Max and I discussed two implications of these results: (1) it’s dangerous to extrapolate from short-lived climate perturbations, like volcanic eruptions, to long-lived perturbations like CO2 increases, and (2) the feedbacks of models that are ‘tuned’ in some way to the historical record are strongly affected by historical forcing estimates.</p> 

<p>We illustrated two of the implications of our results with toy calculations. First, we calculated the impulse response of the two-box model to a doubling of CO\(_2\). That is, we set \(F\) to \(F_{2XCO2}\) at year 1, and 0 at all other times. We did this calculation 3 times: once with the ensemble-mean parameters from the CMIP5 data, once with the upper ocean heat capacity \(c\) reduced by 25% and once with \(\lambda\) reduced by 25%. In the results (panel a) you can see that changing the heat capacity has a much larger effect than changing \(\lambda\) -- we’re in the ultra-fast regime -- which is almost indistinguishable from the "control" calculation. So if we were trying to fit the temperature response to a short-lived perturbation, like a volcanic eruption, we’d mostly have to focus on the upper ocean heat capacity, and we probably wouldn’t be able to constrain \(\lambda\) very well.</p> 

<img src="http://nicklutsko.github.io/notes/images/brute_search_result.jpg" alt="Toy Calculations" style="position:absolute; left:100px; width:576px;height:432px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>Our second toy calculation showed how that feedbacks of “tuned” models are strongly influenced by historical forcing estimates. We illustrated this through “historical” simulations of the 20th century with the two-box model, forcing it with an estimate of the total radiative forcing over the 20th century, \(\Delta F\) (panel b). We then varied the forcing by up to \(\pm\)1 standard deviation of \(F_{2XCO2}\), by setting \(\Delta F(t) = \Delta F(t) + \beta std(F_P2XCO2})\), where \(\beta\) was varied from -1 to 1 in increments of 0.1. For each forcing estimate, we set \(c\), \(c_0\), \(\lambda\) and \(\gamma\) to their ensemble-mean values and searched for the value of \(\lambda\) that gives the best fit to the 20th century temperature record. The lower right panel of the figure shows how the optimal value of \lambda varies as a function of the final forcing at the end of the 20th century (circles), with a linear least-squares regression giving that a 1% change in the estimate of the net forcing resulting in a 1.84% change in the optimal value of \(\lambda\).</p> 

<p>This calculation ignore things like the different forcing efficacies of greenhouse gases, the historical aerosol forcing and internal variability, but show how sensitive the radiative feedbacks in models that are tuned by fitting to the historical temperature record are to assumptions made about the forcing over the 20th century. If you believe our toy calculations then tuning the same model twice using historical forcing estimates that differed by 20% would give values of \(\lambda\) would differ by 37%.</p> 

















