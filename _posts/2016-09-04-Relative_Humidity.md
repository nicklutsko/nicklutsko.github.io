---
layout: post
title: "Relative Humidity in the Tropics"
date: 2016-09-04
use_math: true
---

<p>Many of our predictions for how climate will change under higher CO<sub>2</sub> levels assume that relative humidity stays roughly constant in the tropics. Just one example of the power of this assumption is that it can be used to significantly reduce the spread between model estimates of some of the feedbacks controlling Earth's climate sensitivity $($<a href="http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-15-0352.1">Caldwell et al, 2016</a>$)$. There are a lot of different justifications for the fixed relatively humidity assumption. Recently David Romps laid out an analytical model for relative humidity in the tropics, which can then be used to explain why relative humidity varies little under global warming. I'm going to try to summarize it here.</p>

<h2>Theory</h2>

<p>The basic picture is of relative humidity being determined by a battle between detraining air from convective plumes, which tries to moisten the environment, and subsiding air, which dries out the environment. Romps defines an inverse length-scale for each of these; call them $d$ and $s$ with units 1 / length. $d$ is kind of like the distance away from a convecting plume which the detraining air travels, while $s$ is the water vapor lapse rate -- water vapor will decrease with altitude. After some algebra, the relative humidity can be approximated as
$$
RH = \frac{d}{d + s}.
$$
So what sets $s$ and d? $s$ is actually straightforward to derive using the Clausius-Clapeyron equation and hydrostatic balance, to get
$$
s = \frac{L\gamma}{R_vT^2} - \frac{g}{R_dT}
$$
where $L$ is the latent heat of vaporization, $\gamma$ is the temperature lapse rate, $R_v$ is the specific gas constant of moist air, $T$ is temperature, $g$ is gravitational acceleration and $R_d$ is the specific gas constant of dry air.</p> 

<p>There's some subtlety to this. How $s$ varies with temperature depends on how large the temperature change is. But more importantly, since moisture is present \gamma is actually proportional to s. Romps eventually gets an equation for \gamma which doesn't depend on s, but it's quite messy and depends on the entrainment and detrainment rates. Just thinking intuitively though, \gamma will get larger the drier the air is, so $s$ will increase $($and the relative humidity will decrease!$)$.</p>

<p>$d$ is harder to get a handle on. Simulations and observations suggest that typical values are between \sim200m$^{-1}$ and 2km$^{-1}$ through most of the troposphere. At the height of the anvil, where the cloud spreads out, $d$ clearly gets very large, overwhelming s, and so the relative humidity will be large in the upper troposphere. Apart from this, we don't have much of a theory for $d$ and so the theory isn't actually closed.</p> 

<p>A caveat is that to get equation 1 we have to assume that condensates rain out immediately. If they don't then they could be re-evaporated, which clearly affects the humidity. If we define $\alpha$ as the fraction of condensate that is re-evaporated, then if $\alpha = 1$ the relative humidity goes to 1 and if it is zero then we get equation 1 again. Romps suggests that $\alpha$ will generally not affect the results, qualitatively at least.</p>

<h2>Typical Vertical Profiles</h2>

<p>One of the things Romps is interested in explaining is the "C" shape of vertical relative humidity profiles: the relative humidity is largest close to the surface and in the upper troposphere, with a maximum of about 90\%, and then there is a minimum of around 30\% in the mid-troposphere. This can be explained by thinking about how $s$ and $d$ change vertically.</p>

<p>When going from the surface to the mid-troposphere the lapse rate increases and the change in temperature is large, so the first term dominates and $s$ increases, while $d$ is roughly constant. So the relative humidity will decrease. In the upper troposphere the first term of equation 2 dominates, and $s$ goes to roughly 1km$^{-1}$. However, as discussed above, in the anvil $d$ is very large, so the relative humidity gets large again.</p>

<p>In the lower- to mid- troposphere $s$ ~ 0.3km$^{-1}$ and the minimum and maximum values of the relative humidity are set by the value of d. Using the values above, this sets the limit of relative humidity at $0.2 / (0.2 + 0.3)  = 0.4$ and $2 / (2 + 0.3)$ = 0.9.</p>


<h2>Response to Global Warming</h2>

<p>Using typical values, Romps estimates that relative humidity would increase by 0.003 - 0.008 per degree warming at 300K $($at 1 bar$)$. If RH = 80% at 300K then at 301K it will be 80.3-80.8%. So this is encouraging for the theory.</p>

<p>One way of explaining this is that, assuming entrainment and detrainment are fixed, the relative humidity is just a function of temperature. Increasing the surface temperature then "exposes" more of the high temperature part of the temperature-RH curve. Since the curve is relatively flat near 300K, relative humidity doesn't change much near the surface, while the minimum relative humidity will just move higher up in the atmosphere, though its value will stay constant.</p> 


<h2>Caveat: Entrainment and Detrainment Rates</h2>

<p>There are a lot of really neat ideas in this paper, but the big open questions are entrainment and detrainment. We don't really have first-principle explanations for these, except in the anvil, so we have to rely on estimates and we also have to assume that they are relatively unchanged under global warming. This seems to be one of the main outstanding issues in convection, and there don't seem to be obvious ways of developing deeper theories for them. Maybe "emergent constraint"-type thinking would be useful?</p>












