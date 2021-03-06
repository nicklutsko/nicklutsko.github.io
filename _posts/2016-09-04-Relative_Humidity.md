---
layout: post
title: "Relative Humidity in the Tropics"
date: 2016-09-04
---

<p>Many of our predictions for how climate will change due to higher CO<sub>2</sub> levels assume that relative humidity stays roughly constant in the tropics. Just one example of the power of this assumption is that it can be used to significantly reduce the spread across models in some of the feedbacks controlling Earth's climate sensitivity (<a href="http://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-15-0352.1">Caldwell et al, 2016</a>). Although there is no universally accepted explanation for why relative humidity should remain fixed, a <a href="http://romps.berkeley.edu/2013/lapse/13lapse.pdf">recent paper</a> by David Romps laid out an analytical model for relative humidity in radiative-convective equilibrium which can be used to estimate how relative humidity varies under global warming.</p>

<h3>Theory</h3>

<p>The basic picture is of relative humidity being determined by a battle between air that is detrained from convective plumes, which tries to moisten the environment, and subsidence in non-convecting regions, which dries out the environment. Romps defines inverse length-scales for each of these, I'll call them \(d\) and \(s\) respectively, with units 1/length. \(1 / d\) is the scale over which convection moistens the environment to saturation, and acts like an efficiency parameter, with large \(d\) implying that the convection quickly moistens the environment. \(1 / s\) is the water vapor lapse rate (water vapor decreases with altitude). After some algebra, the relative humidity can be approximated as
$$
RH = \frac{d}{d + s}.
$$
So what sets \(s\) and d? \(s\) is actually straightforward to derive using the Clausius-Clapeyron equation and hydrostatic balance, giving
$$
s = \frac{L\Gamma}{R_vT^2} - \frac{g}{R_dT}
$$
where \(L\) is the latent heat of vaporization, \(\Gamma\) is the temperature lapse rate, \(R_v\) is the specific gas constant of moist air, \(T\) is temperature, \(g\) is gravitational acceleration and \(R_d\) is the specific gas constant of dry air.</p> 

<p>There's some subtlety to this. For instance, how \(s\) varies with temperature depends on how large the temperature change is. More importantly, the lapse-rate \(\Gamma\) is actually proportional to \(s\), since moisture is present. Romps eventually gets an equation for \(\Gamma\) which doesn't depend on \(s\), but it's quite messy and depends on the entrainment and detrainment rates. Just thinking intuitively though, \(\Gamma\) will be larger for drier air, so \(s\) will increase and the relative humidity will decrease.</p>

<p>\(d\) is harder to get a handle on. At the height of the anvil, where the cloud spreads out, \(d\) must be large and so we expect \(d\) to overwhelm \(s\) and the relative humidity to be large. But apart from this we can't say much about \(d\) and so the theory isn't actually closed. From high resolution simulations and observations, typical values are between ~200m\(^{-1}\) and 2km\(^{-1}\) through most of the troposphere.</p> 

<p>A caveat is that this assumes condensates rain out immediately. If they don't then they could be re-evaporated, which clearly affects the humidity. This can be incorporated into the theory using a parameter \((\alpha)\) which is the fraction of condensate that is re-evaporated as it falls. If \(\alpha = 1\) the relative humidity goes to one everywhere and if it is zero then we get the first equation again. Romps shows that the theory is qualitatively unchanged by including \(\alpha\).</p>

<h3>Typical Vertical Profiles</h3>

<p>One of the things Romps is interested in explaining is the "C" shape of vertical relative humidity profiles: the relative humidity is largest close to the surface and in the upper troposphere, with a maximum of about 90%, and there is a minimum of around 30% in the mid-troposphere. This shape comes about because of how \(s\) and \(d\) change with altitude.</p>

<p>When going from the surface to the mid-troposphere the lapse rate increases and the change in temperature is large, so \(s\) increases and, assuming that \(d\) is roughly constant, the relative humidity will decrease. But eventually \(s\) stablizes at about 1km\(^{-1}\), because \(\Gamma\) is just the dry adiabatic lapse rate. At the same time, \(d\) starts to increase close to the anvil and so the relative humidity gets large again in the upper troposphere. This gives us the C shape.</p>

<p>We can also calculate what we expect the maximum and minimum relative humidities to be. Taking \(s\) ~ 0.3km\(^{-1}\) in the lower troposphere and using the values of \(d\) from before, we get \(0.2 / (0.2 + 0.3)  = 0.4\) and \(2 / (2 + 0.3)\) = 0.9, close to what is observed.</p>


<h3>Response to Global Warming</h3>

<p>The hope is that this theory predicts a small change in relative humidity under a global warming scenario, since this is what models tell us. Using typical values, Romps estimates that relative humidity would increase by 0.003 - 0.008 per degree warming at 300K (at 1 bar): if RH = 80% at 300K then at 301K it will be 80.3-80.8%. So this is encouraging for the theory.</p>

<p>An intuitive way of thinking about this is that, assuming entrainment and detrainment are fixed, the relative humidity is just a function of temperature, i.e., there is an invariant temperature-RH curve. Increasing the surface temperature then "exposes" more of the high temperature part of this temperature-RH curve. Since the curve happens to be relatively flat near 300K, relative humidity doesn't change much near the surface. Similarly, the minimum relative humidity in the C just moves higher up in the atmosphere and its value stays constant.</p> 


<h3>Entrainment and Detrainment Rates</h3>

<p>There are a lot of really neat ideas in this paper, but the big open questions are the entrainment and detrainment rates. We don't really have first-principle explanations for these, so we have to rely on observational/modelling estimates, and we also have to assume that they are relatively unchanged under global warming. This seems to be the main outstanding issue in convection, and there don't seem to be obvious ways of developing strong constraints on their values. Maybe "emergent constraint"-type thinking would be useful?</p>












