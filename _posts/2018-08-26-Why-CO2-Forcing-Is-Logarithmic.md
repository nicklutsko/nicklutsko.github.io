---
layout: post
title: "Why The Radiative Forcing of CO2 is a Logarithmic Function of Atmospheric CO2 Concentrations"
date: 2018-08-26
use_math: true
---

<p>One of our basic assumptions about global warming is that the radiative forcing by CO$_2$ -- the outgoing longwave radiation absorbed by atmospheric CO$_2$ -- is a logarithmic function of the atmospheric CO$_2$ concentration: if the radiative forcing of doubling CO$_2$ is $F$, then the radiative forcing of quadrupling CO$_2$ is $2F$.</p>

<p>The conventional explanation for this comes from the details of absorption spectra. Greenhouse gases have absorption lines, particular wavelengths at which they absorb electromagnetic radiation. As the concentration of a gas increases the absorption eventually saturates and there's no more radiation at that wavelength to absorb. But absorption lines have a finite width, so although the absorption is maximum at one wavelength, it decays exponentially away to either side of that wavelength. Once the center wavelength is saturated the absorption is mostly in the "wings" and the forcing increases logarithmically as the concentration of the greenhouse gas is further increased. Present day levels of CO$_2$ are high enough that the main absorption band -- the 15$\mu$m wavelength -- is saturated, so most of the additional absorption comes from the wings.</p>

<p>This explanation relies on integrating over the wings, however, and <a href="https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1002/2014JD022466">Huang and Shahabadi $($2014$)$</a> give a simple argument for why we would expect this to hold even for monochromatic radiance, i.e., at a single wavelength.</p>

<p>Ignoring scattering, the top-of-atmosphere outgoing radiation $R$ is the integral over the atmospheric source functions, multiplied by the transmission function. Working in optical depth co-ordinates $(\tau)$, this is
$$
R = \int^{\tau_s}_0 B(T(\tau))e^{-\tau}d\tau,
$$
where $B(T(\tau))$ is the source function and the transmission function is $e^{-\tau}$.  For an optically-thick atmosphere, we only have to worry about regions near where $\tau = 1$, so we can approximate this equation as
$$
R \approx \int^{\tau = 1+}_{\tau = 1-} B(T(\tau))e^{-\tau}d\tau.
$$
Increasing the concentration of a greenhouse gas, say CO$_2$, is equivalent to making a co-ordinate transform $\tau' = a\tau$, so that
$$
R' \approx \int^{\tau' = 1+}_{\tau' = 1-} B(T(\tau'))e^{-\tau'}d\tau'.
$$
The change in $R$ from this increase, the radiative forcing, is then
$$
\Delta R = R' - R \approx \int^{\tau' = 1+}_{\tau' = 1-} B(T(\tau'))e^{-\tau'}d\tau' - \int^{\tau = 1+}_{\tau = 1-} B(T(\tau))e^{-\tau}d\tau = \int^{\tau = 1+}_{\tau = 1-} B(T(\tau / a))e^{-\tau}d\tau - \int^{\tau = 1+}_{\tau = 1-} B(T(\tau))e^{-\tau}d\tau.
$$
Huang and Shahabadi argue that the Planck function in the longwave spectrum is relatively linear for small changes at the temperatures of Earth's atmosphere $(\sim$200K to 300K$)$ so that
$$
\Delta R \sim T(\tau = 1 / a) - T(\tau = 1).
$$
Going from $\tau$ co-ordinates to $z$ co-ordinates using the transform $\tau = c_1e^{c_2 z}$, and also assuming that the lapse-rate $\Gamma = dT/dz$ isn't affected by the increased CO$_2$, then  
$$
\Delta R \sim \Gamma (z(\tau = 1 / a) - z(\tau = 1)) = -\Gamma ln(a),
$$
and so if $\Delta R$ is equal to $F$ for one doubling of $a$, it will be equal to $2F$ for two doublings of $a$.</p> 

<p>Some caveats are that this argument doesn't work for optically-thin atmospheres, since then we can't just focus on levels near $\tau$ = 1. Another key assumption is that $B$ is linearly proportional to $z$. This could break down if the lapse-rate does weird things, and we also assumed that $\Gamma$ doesn't change. Finally, we assumed that the perturbation is uniform in height. CO$_2$ is referred to as a well-mixed greenhouse gas, but how true is this? Do CO$_2$ concentrations really increase uniformly at all levels? I haven't found satisfying evidence that this is the case, though <a href="https://www.atmos-chem-phys.net/11/2455/2011/acp-11-2455-2011.pdf">this paper</a> seems to suggest that it is a reasonable approximation $($it's hard to tell from the figures, which emphasize the stratosphere$)$.</p>

<p>If we believe this explanation, then an interesting implication is that the forcing $\Delta R$ is proportional to the lapse-rate. So we would expect $\Delta R$ to be largest in the subtropics/mid-latitudes, and smallest at high latitudes, where the lapse-rate can even be negative. This is what <a href="https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1002/2015JD024569">Huang, Tan and Xia $($2015$)$</a> found in a follow-up paper, which suggests that the assumptions made in the original argument are OK. This meridional structure in the forcing is important to understand, because it impacts the atmospheric circulation, especially its energy transport $($e.g., <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017JD027221">Huang et al. $($2017$)$</a>$)$, and helps us untangle the causes of the polar amplification of warming $($see <a href="http://www.meteo.mcgill.ca/~tmerlis/publications/henry_linear_rad.pdf">here</a> and <a href="https://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-18-0103.1">here</a>$)$.</p> 













