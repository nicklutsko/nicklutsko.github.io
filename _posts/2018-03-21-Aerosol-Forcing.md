---
layout: post
title: "Historical Aerosol Forcing"
date: 2018-03-21
use_math: true
---

<p>Earth's climate over the past 150 or so years has been strongly affected by humans. The most well known, and important, human perturbation is the increased concentration of CO$_2$ in the atmosphere, which is responsible for the global warming we have experienced, and will continue to experience in the future. But humans have also emitted large amounts of aerosols into the atmosphere. Aerosols actually cool the planet, counteracting the increased CO$_2$ concentrations to some extent, and it's still unclear exactly how much they cooled the planet.</p>

<p>This is a surprisingly important question. If the aerosol effect is large, say a -2Wm$^{-2}$ forcing from pre-industrial to present, it would imply that Earth's surface temperature is very sensitive to greenhouse gas forcing. This would also be worrying since we expect the aerosol forcing to increase more slowly in the future $($because of efforts to reduce pollution$)$, so temperatures would rise more quickly in the future than they have in the past. On the other hand, a small aerosol effect would point to a lower sensitivity. $($Note that there's been a lot of work recently on why it's deceptive to use historical records to estimate Earth's sensitivity, so the magnitude of the aerosol forcing isn't the only thing to consider$)$.</p>

<p>Another reason to worry about the historical aerosol forcing is that climate models are often tuned by comparing with the global-mean surface temperature record from the 20th century. As part of this, models have to be given estimates of how aerosol and greenhouse gas levels varied during this time, making the final parameter settings in models sensitive to our guesses of the historical aerosol forcing.</p>

<p>Why is the aerosol forcing poorly constrained? Because of the classic climate issues: we don't have long enough historical records of aerosol emissions, and even if we did, aerosol processes take place on scales that are much too small to resolve in climate models, so we have to parameterize them. Another issue is that there are natural aerosols $($dust, sea-salt, etc.$)$, so even a "clean" $($human-free$)$ atmosphere has an aerosol forcing, but we don't know how big this background forcing is.</p>

<p>In <a href="https://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-14-00656.1">a study from 2015</a>, Bjorn Stevens tried to get at the historical aerosol forcing indirectly, using several different approaches. This is an intriguing paper: tighter constrains on the aerosol forcing would be a big step forward, so this is a summary of what Stevens did.</p>


<h3>A Simple Model for Aerosol Forcing</h3>

<p>The centerpiece of the paper is a simple model for the global aersol forcing $F$, based on a paper by <a href="http://science.sciencemag.org/content/255/5043/423">Carlson et al. $($1992$)$</a>. The model parameterizes $F$ using the emission of sulfur dioxide $($SO$_2)$, which is useful because we have estimates of SO$_2$ emissions going back to 1750, and consists of a linear term and a logarithmic term:
$$
F = -\alpha SO_2 - \beta ln\left(\frac{SO_2}{\overline{SO_2}} + 1\right),
$$ 
where $\alpha$ and $\beta$ are coefficients and $\overline{SO_2}$ is a natural source of SO$_2$.</p>

<p>The first term is the direct radiative effect of sulfur emissions, and the assumption is that, although the factors that determine $\alpha$ may have varied over time, their net effect is relatively constant when averaged over a long enough period. There is some discussion of the terms that go into $\alpha$, as well as a general discussion of how big we should expect the aerosol direct effect to be. This is based on the fact that over oceans the clear-sky albedo should be larger in the Northern Hemisphere $($where most aerosols are emitted$)$ than over the Southern Hemisphere. Observations show that this asymmetry is quite small, and suggests a direct aerosol effect of -0.15 Wm$^{-2}$. There are a lot of other details here, but the conclusion is that the aerosol direct effect should be relatively small $($>-0.25Wm$^{-2})$, and so $\alpha$ is small as well.</p>

<p>The second term is the aerosol indirect effect, the influence of aerosols on clouds. Here the assumption is that $F$ depends on the cloud droplet number, $N$, which is often related to $SO_2$ via a power law: $N \sim $SO$_2^x$. In fact, in the appendix $F$ also seems to be related to $N$ via a power law. Stevens approximates all this as a logarithm $($I think $x$ is assumed to be less than 1$)$, with the constant $\beta$ representing the conversion from droplet number to a radiative forcing and from $SO_2$ concentration to $N$. There is a lot of uncertainty in all of this, but somehow Stevens claims that the aerosol indirect effect should be $>-0.75$Wm$^{-2}$. It is unclear to me where he gets this number from.</p>

<p>Stevens estimates $\alpha$ and $\beta$ by fitting SO$_2$ to various estimates of what $F$ was at different points in time. The uncertainty is large, but the mean estimate of $F$ is then $-0.5$Wm$^{-2}$. The results of the fitting suggest that the indirect effect has been the main driver of the changes in $F$, and so $F$ has increased logarithmically with SO$_2$ concentrations. By combining this model with an estimate of the historical greenhouse gas forcing, Stevens shows that $F$ must be $>-1.$Wm$^{-2}$ for the total $($aerosols plus greenhouse gases$)$ forcing to be greater than zero between 1850 and 1950. If the total forcing was less than zero, then the 0.3K warming of the Northern Hemisphere over that time would be entirely due to natural variability, which seems implausible.</p>

<p>The end result is an estimate for the aerosol forcing of -0.3Wm$^{-2}$ to -1Wm$^{-2}$, where the upper bound $($-0.3$)$ comes from an obervational study by <a href="https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2009JD012105">Murphy et al</a>. The point of the paper is really the lower bound of -1Wm$^{-2}$; previous estimates, like from the Carlson et al paper, got as high as -2.3Wm$^{-2}$.</p>


<h3>Comparisons with Models</h3>

<p>This lower bound is supported by some comparisons of models to observations. Two specific points are made. First, Stevens looks at temperature trends from 1920 to 1950, a period of rapid warming $($0.09K/dec$)$, little volcanism and during which the aerosol forcing and the greenhouse gas forcing were probably comparable. Comparing with the pre-industrial control simulations, this trend is almost surely externally forced, but most CMIP5 models simulate smaller trends over this time-period. Based on this, Stevens suggests that they are over-estimating the magnitude of the aerosol forcing.</p>

<p>The other comparison is with the asymmetry in the clear-sky albedo. This value is generally much (up to five times) larger in the models than in the observations. This is more evidence that the aerosol forcing is too strong in models.</p>


<h3>Wrap-up</h3>

<p>This is a compelling paper, though it is quite confusing in places. For example, Stevens is trying to constrain the magnitude of the aerosol forcing, but uses previously published estimates to fit the parameters of his model. It is also unclear where Stevens gets a lot of his numbers from, like the -0.3Wm$^{-2}$ to -1Wm$^{-2}$ bound.</p>

<p>For me, the strongest part of the paper is the comparison with the CMIP5 data. Stevens makes a convincing case that the historical aerosol forcing has been overestimated by most of the models (or else the models are way too sensitive to aerosol forcing). The form of the conceptual model is nice, and gives an intuition for how aerosol forcing should behave. I am not convinced that the parameters Stevens estimates for it are reliable, however. The exact form, particularly for the indirect effect, may also be different, though from a conceptual level the model is probably fine.</p>

<p>Although Stevens spends a lot of time showing that the aerosol forcing cannot be that large, his value is still within the IPCC range, whose mean is -0.9Wm$^{-2}$. He's basically just saying it's probably on the low side of the range. Going back to the beginning, this is suggestive of a relatively sensitivity on the lower side of the range, though clearly other pieces of evidence are needed.</p>














