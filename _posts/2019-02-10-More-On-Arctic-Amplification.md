---
layout: post
title: "More on Arctic Amplification"
date: 2019-02-10
use_math: true
---

<p>I’m still trying to understand Arctic amplification – why the Arctic warms up faster than anywhere else when CO$_2$ concentrations are increased. The top panels of this plot show DJF temperature profiles over land regions, ocean regions and ice regions north of 65$^\circ$N for an RCP8.5 scenario simulation with the GFDL-CM3 model.  $($Arctic amplification is mainly seen in Northern Hemisphere winter$)$. The profiles are averaged over each decade of the 21st century, going from 2006-2015 $($blue$)$ to 2086-2095 $($red$)$.</p>

<img src="http://nicklutsko.github.io/notes/images/GFDL-CM3_polar_warming_breakdown.png" alt="GFDL warming" style="position:absolute; left:200px; width:600px;height:400px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


<p>The bottom panels show time series of sea-ice fraction, sea-ice thickness and surface temperatures over the three surfaces. Temperatures over ice and over land warm rapidly, while the ocean warms much more slowly. The same plot for HadGEM2-CC gives a similar picture, though there is more warming over the ocean.</p> 

<img src="http://nicklutsko.github.io/notes/images/HadGEM2-CC_polar_warming_breakdown.png" alt="HadGEM warming" style="position:absolute; left:200px; width:600px;height:400px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>I think this is because the sea-ice is more “binary” in the GFDL model – grid-boxes tend to be with all ice or all ocean – whereas the HadGEM model has more intermediate values of sea-ice fraction. Since I average by doing 1 – sea-ice fraction, etc. there might be more aliasing of open ocean temperatures and sea-ice temperatures in this model.</p> 

<p>In any case, both simulations suggest that diminishing sea-ice cover is an important component of Arctic amplification. Interestingly, the sea-ice fraction collapses in both models around 2060 and this corresponds to a rapid warming of land temperatures in the HadGEM model, whereas the collapse doesn’t show up in the temperature time-series of the GFDL model.</p>

<h3>Some other Studies</h3>
Some Other Studies

<p>In a 2009 paper, <a href="https://journals.ametsoc.org/doi/pdf/10.1175/2009JCLI3053.1">Deser et al. </a> compared a control simulation with CAM3 with an ensemble of simulations in which sea-ice concentrations were set to those at the end of the 21st century. $($These sea-ice concentrations came from a coupled model RCP8.5 simulation$)$. SSTs at locations without sea-ice were pinned to the freezing temperature.</p>

<p>This produced a strong warming over the Arctic Ocean and the surrounding continents, and Deser et al calculated heat budgets to understand why this was happening. They found that over the Arctic ocean, the air mainly warmed because of increased heat transfer from the warmer ocean waters. Over land, the air mainly warmed because of horizontal advection of relatively warm air from over the oceans:</p>

<img src="http://nicklutsko.github.io/notes/images/Deser_budget.png" alt="Deser budget" style="position:absolute; left:200px; width:573px;height:564px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>The strongest warming was in the winter months $($NDJF$)$, even though the largest sea-ice reductions were in the fall months $($September and October$)$. But the largest air-surface temperature contrasts are in the winter months, leading to the most warming.</p> 

<p>Another paper demonstrating the importance of sea-ice is <a href="https://www.nature.com/articles/s41467-018-07954-9">Dai et al. $($2018$)$</a>. They managed to eliminate the Arctic amplification in a simulation with the CESM model with CO$_2$ increasing by 1%/year by keeping sea-ice fixed.</p> 

<h3>What About the Radiative Forcing?</h3>

<p><a href="http://web.mit.edu/~twcronin/www/document/CroninJansen2015.pdf">Cronin and Jansen</a> showed that in the radiative-advective model for a gray ideal gas, radiative forcing can cause the kind of surface-amplified warming seen in the first two figures of this post. The cooling of the stratosphere is also a response to radiative forcing. But <a href="https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2012GL051598">Screen et al. $($2012$)$</a> found that, in a simulation with fixed sea-ice, etc., the strongest response to the direct radiative forcing is in summer $($their Figure 4$)$:</p> 

<img src="http://nicklutsko.github.io/notes/images/Screen_DRF.png" alt="Screen DRF" style="position:absolute; left:200px; width:364px;height:230px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


<p>To get an intuitive feel for why CO$_2$ forcing is strongest in summer, consider the sensitivity of surface temperature to an increase in the optical depth for a gray ideal gas in radiative-advective equilibrium $($equation 19 of Cronin and Jansen$)$:</p>
$$
\frac{\delta T_s}{\delta \tau_0} = \frac{2$($1 - \beta}F_s + (\frac{2b}{b + 1) - \betaF_A}{4\sigma t_s^3$($2 + \beta\tau_0)^2}
$$
<p>Without going into the details, the sensitivity is directly proportional to $F_s$ -- the amount of insolation reaching the surface. This is zero at high latitudes during winter, drastically reducing the sensitivity to the forcing.</p>

<h3>Wrap-up</h3>

<p><a href="https://www.nature.com/articles/s41558-018-0339-y.pdf">Stuecker et al. $($2018$)$</a> showed that horizontal energy transport isn’t a necessary condition of strong polar amplification; “local processes” are enough. Screen et al. showed that high latitudes are most sensitive to radiative forcings in summer, but Arctic amplification is primarily a winter phenomenon. Similarly, the Cronin and Jansen model suggests that the sensitivity of high latitudes to radiative forcing is proportional to the insolation, which is zero in winter.</p>

<p>So this leaves sea-ice loss as the main cause of Arctic amplification. As ice melts, more open ocean is exposed, and there is greater heat transfer from the surface to the lower atmosphere. More warm air is advected over the ice and land-surfaces, which warm. This is a more important effect than the reduction in albedo due to the sea-ice loss. Doing a conventional feedback analysis can suggest Arctic amplification is caused by a strong lapse-rate feedback at high latitudes; and the fact that lapse-rate feedback is negative at low latitudes does contribute to Arctic amplification. But the lapse-rate feedback is really hiding these effects of sea-ice loss, as the Arctic inversion is eroded.</p>

<p>The dependence of Arctic amplification on sea-ice is one reason why it’s difficult to study. Idealized models, which don’t include sea-ice, often show Arctic amplified warming because of changes in meridional heat transports and their corresponding effects on lapse-rates $($see here and here$)$. But this could plausibly be counteracted by the water vapor feedback, which typically isn’t included in gray radiation, “Frierson”-type models. Untangling these different factors in idealized models is useful, but seems to be of secondary importance if the dominant cause of Arctic amplification is sea-ice loss.</p>

<p>$($Thanks to Nadir Jeevanjee for discussions and for pointing me to the Dai paper$)$</p>








