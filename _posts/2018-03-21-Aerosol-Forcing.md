---
layout: post
title: "The Importance of Knowing the Historical Aerosol Forcing"
date: 2018-03-21
use_math: true
---

<p>Earth's climate over the past 150 or so years has been strongly affected by humans. The most well known, and important, human perturbation is the increased concentration of CO$_2$ in the atmosphere, which is responsible for the global warming we have experienced, and will continue to experience in the future. But humans have also emitted large amounts of aerosols into the atmosphere. Aerosols actually cool the planet, counteracting the increased CO$_2$ concentrations to some extent, but it's still unclear exactly how much they cooled the planet by.</p>

<p>This is a surprisingly important question. If the aerosol effect is large, say a -2Wm$^{-2}$ forcing from pre-industrial to present, it would imply that Earth's surface temperature is very sensitive to greenhouse gas forcing. This would also be worrying since we expect the aerosol forcing to increase more slowly in the future (because of efforts to reduce pollution), so temperatures would rise more quickly in the future than they have in the past. On the other hand, a small aerosol effect would point to a lower sensitivity. \(Note that there's been a lot of work recently on why it's deceptive to use historical records to estimate Earth's sensitivity, so we can't just make an inference based on the aerosol forcing\).</p>

<p>Another reason to worry about the historical aerosol forcing is that climate models are often tuned by comparing with the global-mean surface temperature record from the 20th century. As part of this, models have to be given estimates of how aerosol and greenhouse gas levels varied during this time, making the final parameter settings in models sensitive to our guesses of the historical aerosol forcing.</p>

<p>Given all this, why is the aerosol forcing poorly constrained? Because of the classic climate issues: we don't have long enough historical records of aerosol emissions, and even if we did, aerosol processes take place on scales that are much too small to resolve in climate models. Another issue is we don't know what background levels of aerosols (dust, sea-salt, etc.) are.</p>

<p>In <a href="https://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-14-00656.1">a paper from 2015</a>, Bjorn Stevens tried to get at the aerosol forcing indirectly, using several different approaches. I've been intrigued by this paper for a while: tighter constrains on the aerosol forcing would be a big step forward, so here are notes on what Stevens did.</p>


<h3>A Simple Model for Aerosol Forcing</h3>

<p>The first approach Stevens takes is to develop a simple model for the global aersol forcing $F$, based on a paper by Carlson et al. (1992). The model is based on the idea that $F$ can be parameterized using the emission of sulfur dioxide (SO$_2$), which is useful because we have estimates of SO$_2$ emissions going back to 1750. This leads to a very simple equation for $F$, which includes a linear term and a logarithmic term:
$$
F = -\alpha SO_2 - \beta ln(\frac{SO_2}{\SO_2\>} + 1),
$$ 
where $\alpha$ and $\beta$ are coefficients and $\overline{SO_2}$ is a background, natural source of SO$_2$.</p>

<p>The first term is the direct radiative effect of sulfur emissions, and the assumption is that, although the factors that go into $\alpha$ may have varied over time, their net effect is relatively constant when averaged over a long enough period. There is some discussion of the terms that go into $\alpha$, as well as a general discussion of how big we would expect the aerosol direct effect to be. There are a lot of details here, but the conclusion is that the aerosol direct effect should be relatively small \($>-0.25$Wm$^{-2}$\), and so $\alpha$ is small as well.</p>

<p>A useful tool Stevens uses here is the asymmetry in the clear-sky albedo: over oceans the clear-sky albedo should be larger in the Northern Hemisphere (where most aerosols are emitted) than over the Southern Hemisphere. Observations show that this asymmetry is quite small, and suggests a direct aerosol effect of -0.15 Wm$^{-2}$.</p>

<p>The second term is the aerosol indirect effect; the influence of aerosols on clouds. Here the assumption is that $F$ depends on the cloud droplet number, $N$, which is often related to $SO_2$ via a power law: $N \sim $SO$_2^x$ \(I think $x$ is assumed to be less than 1\). Stevens approximates this as a logarithm. There is a lot of uncertainty in the aerosol indirect effect, but Stevens claims that it should be $>-0.75$wm$^{-2}$, though it is unclear to me where he gets this number from.</p>

<p>Stevens estimates $\alpha$ and $\beta$ by fitting SO$_2$ versus various estimates of what $F$ was at different points in time. The uncertainty is large, but the mean estimate of $F$ is then $-0.5$Wm$^{-2}$. The estimate of $\beta$ is much bigger than the estimate of $\alpha$, so the indirect effect is the main driver of the changes in $F$, which increases logarithmically with SO_2. Stevens also shows that the total forcing due to aerosols and greenhouse gases between 1850 and 1950 is unlikely to have been greater than zero unless $F$ is $>-1.3$Wm$^{-2}$. If the total forcing was less than zero, then the 0.3K warming of the Northern Hemisphere over that time would be entirely due to natural variability, which seems implausible.</p>

<p>The end result is an estimate of -0.3Wm$^{-2}$ to -1Wm$^{-2}$, though where Stevens got these numbers from is unclear to me.</p>


<h3>Comparisons with Models</h3>

<p>The other part of the paper is comparing models with observations. Two specific points are made. First, Stevens looks at temperature trends from 1920 to 1950, a period of rapid warming (0.09K/dec), little volcanism and when the aerosol forcing and the greenhouse gas forcing were probably comparable. Comparing with the pre-industrial control simulations, this trend is almost surely externally forced, but most CMIP5 models simulate smaller trends over this time-period. Based on this, Stevens suggests that they are over-estimating the magnitude of the aerosol forcing.</p>

<p>The other comparison is with the asymmetry in the clear-sky albedo. This value is generally much (up to five times) larger in the models than in the observations. This is more evidence that the aerosol forcing is too strong in models.</p>


<h3>Wrap-up</h3>

<p>This is a compelling paper, though it is quite confusing in places. For example, Stevens is trying to constrain the magnitude of the aerosol forcing, but uses previously published estimates to fit the parameters of his model. It is also unclear where Stevens gets a lot of his numbers from, like the -0.3Wm$^{-2}$ to -1Wm$^{-2}$ bound.</p>

<p>For me, the strongest part of the paper is the comparison with the CMIP5 data. Stevens makes a convincing case that the historical aerosol forcing has been overestimated by most of the models (or else the models are way too sensitive to aerosol forcing). The form of the conceptual model is nice, and gives an intuition for how aerosol forcing should behave. I am not convinced that the parameters Stevens estimates for it are reliable, however. The exact form, particularly for the indirect effect, may also be different, though from a conceptual level the model is probably fine.</p>

<p>Although Stevens spends a lot of time showing that the aerosol forcing cannot be that large, his value is still within the IPCC range, whose mean is -0.9Wm$^{-2}$. He's basically just saying it's probably on the low side of the range. Going back to the beginning, this is suggestive of a relatively sensitivity on the lower side of the range, though clearly other pieces of evidence are needed.</p>














