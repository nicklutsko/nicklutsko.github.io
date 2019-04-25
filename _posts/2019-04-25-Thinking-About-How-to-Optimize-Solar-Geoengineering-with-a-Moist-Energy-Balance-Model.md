---
layout: post
title: "Thinking About How to Optimize Solar Geoengineering with a Moist Energy Balance Model"
date: 2019-04-25
use_math: true
---

<p>Solar geoengineering, or solar radiation management $($SRM$)$, is is often proposed as a way of counteracting the global warming effects of increased CO$_2$ concentrations. The idea is that by reducing the amount of incoming solar radiation reaching Earth's surface, we can $($partially$)$ compensate for some of the extra heat trapped by CO$_2$. The main proposed way of doing this is injecting aerosols $($small particles$)$ into the stratosphere, where they would reflect sunlight back to space $($wikipedia page <a href="https://en.wikipedia.org/wiki/Solar_radiation_management">here</a>$)$.</p>

<p>There are a lot of questions, political and scientific, about SRM. One thing which has interested me is how to optimize SRM. That is: how can we implement SRM to best counteract the effects of global warming?</p>

<p>One option is to focus on maintaining the equator-to-pole temperature gradient. This is one of the key features of the climate system, and controls many other aspects of the climate. For instance, the speed and position of the mid-latitude jet-stream are largely set by the temperature gradient. Under global warming we expect the equator-to-pole temperature gradient to weaken, because higher latitudes warm faster than low latitudes. This would cause the jet stream to slow down, and we also expect the jet stream to shift polewards, though the jury is still out on why exactly. Changes in the jet streams could have many consequences for mid-latitude climates..</p>

<p>Many SRM studies consider SRM implementations in which the incoming solar radiation is reduced by 1\% at all latitudes $($let's ignore the engineering question of how to achieve this$)$. However, in the annual-mean the tropics receive more sunlight than the high latitudes, so reducing the solar radiation by the same fraction at all latitudes results in a much larger cooling of the low latitudes than the high latitudes, and the equator-to-pole temperature gradient still increases substantially. Alternatively, we could decrease the incoming radiation by the same amount at all latitudes. This would lead to a more uniform cooling, maintaining the equator-to-pole temperature gradient.</p>

<p>To test these two options, I did some calculations with a simple moist energy balance model $($EBM -- see <a href="http://www.meteo.mcgill.ca/~tmerlis/publications/merlis_ebm_pa.pdf">Merlis and Henry</a> for details$)$. This consists of a single equation:
$$
C \frac{\partial T (\phi)}{\partial t} = \frac{1}{4}QS(\phi)a(\phi) - (A + BT(\phi)) - \nabla\cdot\mathbf{H}(\phi) + F 
$$
where $C$ is the heat capacity of the ocean mixed-layer, $T$ is temperature, $\phi$ is latitude, $t$ is time, $\frac{1}{4}QS(\phi)a(\phi)$ is the incoming radiation as a function of latitude, $A + BT(\phi)$ approximates the radiative feedbacks, $\nabla\cdot\mathbf{H}(\phi)$ is the diffusion of moist static energy $(h)$ and $F$ is some radiative forcing, like that due to increasing CO$_2$ concentrations. I've used the same parameter values as Merlis and Henry, and the script for the calculations is <a href="http://nicklutsko.github.io/code/moist_EBM.py">here</a>.</p>

<img src="http://nicklutsko.github.io/notes/images/moist_EBM_geoengineering.png" alt="moist EBM geoeng" style="position:absolute; left:150px; width:700px;height:350px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>First, I integrated the moist EBM to equilibrium with $F = 0$, giving a surface temperature profile that compares reasonably well with what we see on Earth $($panel b of the Figure$)$. The temperature response to a uniform forcing of 4Wm$^{-2}$ is shown by the blue curve in panel e. This also looks like a typical global warming response, with the warming amplified at high latitudes. I then did two more experiments with the solar constant $($$Q$$)$ reduced uniformly by 2Wm$^{-2}$ and with $Q$ reduced by 1\% $($see panel d for the changes in insolation$)$.</p>

<p>The temperature responses in these two cases $($orange and red lines in bottom left panel$)$ confirm that the equator-to-pole temperature gradient increases more when $Q$ is reduced by 1% compared to a uniform reduction in $Q$. </p>

<p>But even with a uniform reduction, there is greater warming at high latitudes. The reason for this is that the moist static energy, $h$, depends on moisture as well as temperature. In a warmer world moisture increases faster at low latitudes than at high latitudes, following the Clausius-Clapeyron relation, and $h$ does as well. Since the MSE gradient increases, more MSE is diffused to higher latitudes, which warm up more as a result. So to really maintain the equator-to-pole temperature gradient we would actually want to reduce the insolation more at high latitudes than at low latitudes.</p>

<p>This is an idealized calulation, but <a href="https://iopscience.iop.org/article/10.1088/1748-9326/5/3/034009/pdf">Ban-Weiss and Caldeira $($2010$)$</a> looked into this problem using NCAR CAM3.1 atmospheric model, trying to optimize the sulphate aerosol distribution to minimize the perturbation to surface temperatures, and also found that a greater reduction at high latitudes is needed. Interestingly, they also tried to optimize to reduce the perturbations to the hydrologic cycle, which they defined as precipitation minus evaporation $($P - E$)$. They found it harder to minimze P - E, and also found that a more uniform distribution of aerosols was needed, corresponding more closely to the 1% case.</p>

<p>Can we understand this using the moist EBM? Neglecting changes in moisture transports, the change in $P - E$ can be approximated as:
$$
\Delta $($P - E$)$ = \alpha\Delta T$($P - E$)$
$$
where $\alpha \sim$7%K$^{-1}$ $($this comes from <a href="https://journals.ametsoc.org/doi/pdf/10.1175/JCLI3990.1">Held and Soden, 2006</a>$)$. So the changes are large where the climatological $P - E$ is large. Panel c of the Figure shows the climatological P - E in the Northern Hemisphere, calculated from the MERRA reanalysis dataset. This is largest in the tropics and subtropics, then tapers off at higher latitudes. Panel f shows the responses of $P - E$ for each of the three calculations, with the largest changes in the tropics, as expected. Both of the SRM schemes substantially reduce the change in $P - E$, but the 1\% run reduces it more than the uniform run. The reason for this is that the 1\% run has a larger temperature change at low latitudes, where the change in $P - E$ is largest. At higher latitudes the two cases are very similar, since the change is anyways very small.</p>

<p>So there seems to be a trade-off between minimizing the temperature perturbations and minimizing the perturbations to the hydrologic cycle. These roughly correspond to an emphasis on cooling high latitudes more or cooling the tropics more. And of course this is all an annual-mean and zonal-mean picture. We could also worry about regional climates, like minimizing the disruption of the monsoons. Even before thinking about the engineering question of how to maintain these aerosol distributions, this seems like a really tricky problem.</p>






