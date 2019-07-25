---
layout: post
title: "Why is the Weather Only Predictable for 2 Weeks at Most?"
date: 2019-07-25
---

<p>Someone asked me recently about the difference between weather and climate. When do we call it “weather” and when is it “climate”? And how can we predict the climate 10 or 100 years from now, when it’s so hard to predict the weather a week from now?</p>

<p>As part of this conversation it came up that, even with a perfect weather model, tiny errors in the observed state of the atmosphere mean that we’d only be able to get accurate forecasts for up to about two weeks. For longer lead-times the model would lose all skill, until we asked about seasonal time-scales: we can safely predict that summer will be warmer than winter.</p>

<p>The reason for this is that errors – either problems with the model or with the observations used to initialize the model – grow faster at smaller scales than they do at larger scales. This can be quantified through doubling times: error takes much longer to grow from some scale \(x\) to \(2x\) than from \(x/2\) to \(x\). This puts a limit on the atmosphere’s predictability, since at a certain point the improvements from increasing resolution and improving data quality are negligible.</p>

<p>As an example, imagine we had a weather model and observations that were accurate down to 10km resolution, and we said the model became unusable once the errors reached a scale of 100km. If we improved the resolution down to 5km, any initial errors would grow so quickly that we’d only get a small increase in the forecast lead time compared to the 10km model and observations:</p>

<img src="http://nicklutsko.github.io/notes/images/predictability_example.png" alt="Predictability example" style="position:absolute; left:100px; width:678px;height:240px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>The “finite” predictability of the atmosphere, caused by the rapid doubling times at small scales, was first shown by Ed Lorenz in a <a href="https://onlinelibrary.wiley.com/doi/abs/10.1111/j.2153-3490.1969.tb00444.x">1969 paper</a>. Plugging in some numbers, Lorenz did a back-of-the-envelope calculation to estimate that the predictability of the atmosphere is limited to about 2 weeks at most.</p> 

<h3>A Problem with Lorenz's Theory</h3>

<p>In 2008, <a href="https://journals.ametsoc.org/doi/full/10.1175/2007JAS2449.1">Rotunno and Snyder</a> showed that there was a problem with Lorenz’s derivation. As part of this derivation, Lorenz had to assume something about the kinetic energy (KE) spectrum of atmospheric turbulence. The KE spectrum is the amount of kinetic energy contained at each wavenumber \(k\) (the inverse wavelength) of the turbulence and is typically assumed to follow a power law:
$$
E \sim k^{-p}
$$
Lorenz was working with 2D turbulence (the aspect ratio of the atmosphere is so large that we can treat it as being ~2D) and assumed \(p = -5/3\): 
$$
E_L \sim k^{-5/3}
$$
following Kolmogorov’s classic result for 3D turbulence.</p> 

<p>Lorenz’s derivation relies on this 5/3 power to show that errors grow faster at smaller scales. But for 2D turbulence \(p\) is actually equal to 3: 
$$
E_L \sim k^{-3}
$$
(note: the \(k^{-3}\) scaling was discovered around the same time as Lorenz did his calculations).</p>

<p>Substituting the \(p = -3\) spectrum into the derivation gives “infinite” predictability: the rate of error growth is independent of scale, so that going from a 10km model to a 5km model increases the lead time by a factor of 2.  If \(E\) is proportional to a higher power than 3, errors take longer to grow at small scales than at large scales and using a better model gives a large increase in lead time.</p>

<p>To see the difference, Rotunno and Snyder compared the growth of error energy for \(k^-5/3\)  and \(k^-3\) spectra:</p>

<img src="http://nicklutsko.github.io/notes/images/Rotunno_Snyder_2008.png" alt="Rotunno and Snyder" style="position:absolute; left:230px; width:493px;height:240px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>(Figure 1 from Rotunno and Snyder, 2008.)</p> 

<p>In the \(k^{-3}\) case the error growth is roughly constant in time in wavenumber space, whereas for \(k^{-5/3}\) the error grows much faster at high wavenumbers than at low wavenumbers (large scales).</p> 

<h3>A Problem with Lorenz's Theory</h3>

<p>To get back to the 2 week predictability barrier, Rotunno and Snyder noted that observations show that on scales smaller than about 1000km, the atmosphere roughly follows \(k^{-5/3}\) scaling:</p> 

<img src="http://nicklutsko.github.io/notes/images/Gage_Nostrom_spectra.png" alt="Atmospheric spectra" style="position:absolute; left:230px; width:454px;height:448px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

<p>(Figure 1 from <a href="https://journals.ametsoc.org/doi/pdf/10.1175/1520-0469%282003%29060%3C0824%3ATKAKES%3E2.0.CO%3B2">Tung and Orlando (2003)</a>, note that the meridional wind and potential temperature data have been offset by a constant factor so they can all be plotted on the same figure.)</p> 

<p>It’s thought that in this regime the atmosphere is best represented by surface quasi-geostrophic (SQG) turbulence, which is a kind of intermediate between 2D and 3D turbulence. See <a href="http://pordlabs.ucsd.edu/wryoung/theorySeminar/pdf14/HeldPierrehumbert.pdf">here</a> for more. The kinetic energy spectrum for SQG has a \(k^{-5/3}\) scaling and so there is a finite predictability barrier.</p> 

<h3>Error Growth as Turbulent Dispersion</h3>

<p>The derivations by Lorenz and Rotunno and Snyder are long and technical, so it’s hard to get an intuitive feel for the difference between these different kinds of turbulence. Instead, I like to think about error growth as being like the dispersion of a passive tracer in a fluid: imagine two small patches of “error” in the atmosphere, how quickly do these move apart?</p> 

<p>There is some classic literature on turbulent dispersion, going back to (at least) <a href="https://royalsocietypublishing.org/doi/abs/10.1098/rspa.1926.0043">Richardson (1926)</a>, who derived the “4/3” law. If we think of dispersion as a diffusive process, then a scaling for the diffusivity is:
$$
D \sim \sqrt{E l}
$$
where \(l\) is a length scale (the separation between the particles) and \(E\) is the kinetic energy density (units of energy/unit wavenumber or energy \(\times\) length). Substituting in \(E \sim k^{-5/3} = l^{5/3}\) then gives
$$
D \sim l^{4/3}.
$$
We can get a characteristic spreading time-scale by dividing \(l^2\) by \(D\):
$$
t \sim l^2 / D \sim l^{2/3}
$$
So the characteristic spreading time-scale is longer for larger scales or distances (though the dependence is less than linear). Substituting the \(k^{-3}\) (\(l^3\)) spectrum instead gives
$$
D \sim \sqrt{E_{2D} l} \sim \sqrt{l^4} = l^2
$$
and hence
$$
t \sim l^2 / D \sim l^0
$$
</p> 

<p>The spreading time-scale is now independent of length-scale, just as Rotunno and Snyder found in their formal derivation. You can also see that if \(p\) is greater than 3 the error spreading time is longer for smaller scales. (Note that an issue with what I’ve done here is it treats the error as a passive tracer – is it better to treat it as an active tracer?).</p> 

<p>So one way of thinking about predictability is that it depends on how quickly errors diffuse to larger scales. In 2D turbulence the diffusivity grows as distance \(l^2\), which is fast enough that the doubling time is roughly constant as a function of scale, but for 3D turbulence and SQG, which are a better match for the observed atmosphere, the diffusivity grows more slowly, proportional to \(l^{4/3}\), and so the doubling time increases for larger scales.</p> 

<p>(Thanks to Chris Lutsko for feedback on an earlier version of this post.)</p>






















