---
layout: post
title: "Why Doesn’t the Tropical Atmosphere Superrotate?"
date: 2019-08-23
---

<p>"Superrotation" refers to atmospheric flows that rotate more quickly than the planet beneath them, such that there is an angular momentum maximum in the interior of the atmosphere. Earth rotates west-to-east and this rotation is fastest at the equator, so a superrotating atmosphere has west-to-east winds (\(u > 0\)) at the equator. At higher latitudes the rotation is slower, so superrotation requires faster flow. Mathematically, the angular momentum (\(M\)) for a shallow atmosphere is:
$$
M = (u + \Omega a cos\theta)acos\theta,
$$
where \(\Omega\) is the angular velocity at the Equator, \(a\) is Earth's radius and \(\theta\) is latitude. At the equator, the surface angular momentum is \(M = \Omega a^2\), so uperrotating flow has 
$$
u_s > \Omega sin^2(\theta) / cos\theta.
$$</p>

<p>Hide's theorem tells us that the mean flow cannot maintain a superrotation state, so the only way to create superrotation is with (upgradient) eddy momentum fluxes. This turns out to be pretty common: the atmospheres of Venus, Jupiter, Saturn and Titan superrotate. People also get excited about superrotation because of the potential for bistability. Simple models often show hysteresis, where a superrotating and non-superrotating state co-exist for certain model parameters. (There are even ideas that superrotation was important for paleo climates.)</p>

<p>So why doesn’t Earth’s atmosphere superrotate? To answer this, we have to go through the terms in Earth’s zonal-mean angular momentum budget:
$$
\frac{\partial \bar{u}}{\partial t} = &f[\bar{v}] - [\bar{v}]\frac{\partial [\bar{u}]}{\partial y} - [\bar{\omega}]\frac{\partial[\bar{u}]}{\partial p} - \frac{\partial}{\partial y}\left([\bar{u}^*\bar{v}^*]\right) -\frac{\partial}{\partial p}[\bar{u}^*\bar{\omega}^*] - \frac{\partial}{\partial y}[\overline{u'v'}] - \frac{\partial}{\partial p}[\overline{u'\omega'}],
$$
where \(v\) is the meridional (south-north) velocity, \(\omega\) is the pressure velocity, overbars are zonal means, square brackets are time-means, asterisks are zonal anomalies and \('\)s are anomalies from the time-mean. For simplicity I've also written the budget out in cartesian co-ordinates and left out the the vertical Coriolis term, the metric terms and surface friction.</p>

<p>This leaves the \(fv\) term and then terms corresponding to the divergence of momentum by the mean horizontal flow, the mean vertical flow, the stationary eddy horizontal flow, etc. The horizontal transient term can be broken down further into a transient zonal-mean term and a transient eddy term:
$$
[\overline{u'v'}] = [\overline{u'^*v'^*}] + \overline{[u'][v']}.
$$</p>
In a <a href="http://www.meteo.psu.edu/~sxl31/papers/Lee99.pdf">paper from 1999</a>, Sukyoung Lee showed that these transient terms are key. Here I've updated one of the figures, showing the budget at 200hPa, using data from the MERRA reanalysis:</p>

<img src="http://nicklutsko.github.io/notes/images/annual_mean_superrotation_budget.png" alt="Superrotation budget" style="position:absolute; left:150px; width:300px;height:450px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br />

The main balance is between the transient eddies which accelerate the zonal-mean flow at the equator, and transient fluctuations of the mean flow, which decelerate the flow. (Note that the mean vertical term is important lower in the atmosphere, as the rising branch of the HC brings up high angular-momentum air.)</p>

<p>What do these transient terms represent? Pablo Zurita Gotor looked into the tropical eddy momentum fluxes in two papers last year (<a href="https://journals.ametsoc.org/doi/full/10.1175/JAS-D-18-0297.1">here</a> and <a href="https://journals.ametsoc.org/doi/full/10.1175/JAS-D-18-0304.1">here</a>), and found that they have a pretty complicated structure. The dominant term seems to be interactions between tropical stationary waves and zonal-anomalies in the Hadley circulation (HC, i.e., between the rotational zonal velocity and the divergent meridional velocity). On shorter time-scales, interactions between the MJO and the anomalous Hadley circulation also converge momentum into the equator, but this effect is smaller.</p> 

<p>These fluxes are balanced by fluctuations in the zonal-mean flow, which really just means the seasonal cycle of the HC. Here’s what the angular momentum transport (\(\overline{[u'][v']}\)) by the HC looks like over the course of the year (top panel):</p> 

<img src="http://nicklutsko.github.io/notes/images/seasonal_cycles_equator.png" alt="Seasonal cycle equator" style="position:absolute; left:150px; width:500px;height:400px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br />

<p>You can see that it fluxes a lot of momentum across the equator in summer and in winter. In summer, the flow is anomalously negative (\(u' 0\)) and the meridional flow is to the south (\(v'  0\)), so momentum is diverged out of the HC. Similarly in winter \(u' >0\) and \(v' > 0\) (the ITCZ is south of the equator), and momentum is again converged into the equator.</p>

<p>In the annual-mean, the Hadley circulation is north of the equator, from Lindzen and Hou (1980), we know that this means it will have less angular momentum, which partly explains why the meridional component of the HC opposed superrotation. But interestingly, when you look at the actual value of the winds, there is superrotation, on average, in winter (bottom panel of above figure).</p>

<p>Calculating the angular momentum budget for November (when the winds are accelerating) indicates that stationary waves are driving the superrotation. </p> 
<img src="http://nicklutsko.github.io/notes/images/November_superrotation_budget.png" alt="November superrotation budget" style="position:absolute; left:150px; width:300px;height:450px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br />

<p>So the lack of superrotation is due to the seasonal cycle of the HC, which counteracts the stationary wave fluxes. Interestingly, both the stationary waves and the HC cycle are driven by the differences between the Northern Hemisphere and the Southern Hemisphere. That is, since the NH is warmer than the SH, the time-mean ITCZ is north of the equator, and the seasonal cycle of the HC damps the superrotation. But the land in the Northern Hemisphere excites the stationary waves.</p> 

<p>This is an uneasy balance, and it seems like it could easily change, but for now, tropical waves and the tropical HC balance each other out. Is there a fundamental reason for this? To answer this, we need better theories for zonal anomalies in the HC.</p> 



