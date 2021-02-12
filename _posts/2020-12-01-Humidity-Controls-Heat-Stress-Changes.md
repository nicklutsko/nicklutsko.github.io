---
layout: post
title: "Simple Models of Delayed Warming in the East Pacific"
date: 2020-12-01
---

Changes in heat stress could be one of the most devastating impacts of climate change, with a wide variety of impacts on humans and ecosystems. As just one example, <a href="https://static1.squarespace.com/static/55667009e4b04bbb290cc837/t/5b6b13098a922dee4a0ffb26/1533743898517/Science-2015-Hsiang-Kopp-Jina-Rising.pdf">Hsiang et al</a> suggest that increased mortality associated with rising heat stress is likely to be the most economically-damaging consequence of climate change on North America (see their Figure 5b).

<p>To start thinking about heat stress, I wanted to understand what controls how it changes with warming. I knew that temperature is important, but also that humidity plays a role. Working through some simple scalings, I eventually found that, surprisingly, changes in specific humidity are generally the main driver of changes in heat stress, not changes in temperature. This is because specific humidity increases by O(7%/\(^\circ\)C), whereas temperature only increases by O(1/3%/\(^\circ\)C) (=1/300). The larger fractional changes in specific humidity will win out over changes in temperature in all but the coldest, driest climates, though the definitions of "cold" and "dry" depend on the relative weightings of temperature and humidity by a given heat stress metric.</p>  

So understanding and predicting changes in heat stress seems to mostly come down to understanding and predicting changes in specific humidity. Similarly, model biases in heat stress will mostly be caused by biases in their specific humidity distributions. In a <a href="https://journals.ametsoc.org/view/journals/clim/aop/jcliD200262/jcliD200262.xml">recent paper</a>, I used these ideas to develop thresholds on where we should expect specific humidity changes or temperature changes to dominate heat stress changes, and I checked these thresholds against CMIP6 and observational data. The following summarizes some of the key points, though there's much more to explore in the published paper (emergent constraints, sources of model bias, etc.).

<h3>Why does humidity matter for heat stress?</h3>

Humans feel heat stress when more heat is input into our bodies than is dissipated back into the environment. If excess heat is input for too long, humans experience hyperthermia and body processes start to shut down. But even mild levels of heat stress can negatively affect health, productivity, ...

<p>The energy input into our bodies is a function of temperature, as we take in more heat in warmer climates. But about 75% of the heat loss from our bodies comes via evaporation, which is mostly controlled by specific humidity. Why specific and not relative humidity? Evaporation is set by the difference between the air's specific humidity and the saturation specific humidity: \(E = q_s - q_a = q_s(1 - RH)\). So even if the relative humidity decreases, the net evaporation goes down if q_s decreases enough. (Side note: I've seen the 75% number in a few different pieces, but I'm not sure where it actually comes from.)</p>

<h3>Larger fractional changes in specific humidity</h3>

<p>Since heat stress is a function of humidity and temperature, we know that changes in both are important. However, we also know that fractional changes in specific humidity will be much larger, and will exhibit a much larger range, than changes in temperature: fractional changes in temperature go from roughly 0.25%/\(^\circ\)C to 0.33%/\(^\circ\)C (1/250 - 1/300). On the other hand, at fixed relative humidity specific humidity increases by 7%/\(^\circ\)C. Over land, where relative humidity is expected to decrease, specific humidity will go up by less than 7%/\(^\circ\)C, and might even decrease with warming. So the range of fractional specific humidity changes is much larger than the range of temperature variations, and specific humidity will show much more regional and/or intermodel variations than the small fractional changes in temperature.</p>

Some heat stress metrics might weigh temperature much more heavily than humidity, so that the larger fractional variations are less important. But eventually, in warm and humid enough climates, specific humidity will be the main driver of heat stress changes.

<h3>Quantifying how temperature and humidity contribute to heat stress</h3>

<p>As a starting point for thinking about heat stress, I like to use equivalent potential temperature, \(\theta_E\), which is closely related to moist static energy and is conserved under moist pseudoadiabatic ascent. Equivalent potential temperature can be approximated as:
$$
\theta_e \approx \theta \exp\left(\frac{L q_v}{c_p T_L}\right),
$$
where $\theta$ is potential temperature, $L$ is the latent heat of warming, $q_v$ is the mixing ratio of water vapor (approximately equal to the specific humidity), $c_p$ is the heat capacity of dry air and $T_L$ is the temperature at the lifting condensation level. Fractional changes in near-surface equivalent potential temperature can then be approximated as
$$
\frac{\Delta \theta_e}{\theta_e} \approx \frac{\Delta\theta}{\theta} + \frac{L}{c_pT}\Delta q_v,
\$${align}
where the second-order $T_L$ term is ignored, and $T_L$ is approximated by the surface temperature $T$.</p>

<p>To get a sense of the relative importance of temperature versus moisture, let's assume near-surface relative humidity stays fixed with warming. In this case, $\frac{\Delta q_v}{q_v} \approx 0.07^\circ\text{C}^{-1} \Delta T$, and substitution gives
\begin{align}
\frac{\Delta \theta_e}{\theta_e} \approx \frac{\Delta\theta}{\theta} + 0.07^\circ\text{C}^{-1}q_v\frac{L}{c_p}\frac{\Delta T}{T} = \frac{\Delta\theta}{\theta} + 174 q_v\frac{\Delta T}{T},
\end{align}
where $q_v$ now denotes the baseline specific humidity. Assuming fractional changes in surface potential temperature are roughly equal to fractional changes in surface temperature (i.e., that surface pressure changes are small), the moisture term will be the primary driver of the fractional change in \(\theta_E\) wherever
$$
q_v > \frac{1}{174} \approx 5.6 \text{gkg}^{-1} = q_{v, 0}.
$$
This is a low baseline specific humidity threshold, which is met throughout most of the tropics, subtropics and mid-latitudes in summer.</p>


<p>This derivation can be easily modified to account for a change in relative humidity, but over land things are a bit trickier. <a href="https://journals.ametsoc.org/jcli/article/29/21/7613/34565/A-Simple-Moisture-Advection-Model-of-Specific">Chadwick et al. (2016)</a> and <a href="http://pog.mit.edu/src/byrne_land_relative_humidity_decrease_2016.pdf">Byrne and O'Gorman (2016)</a> have shown that moisture changes over land can be approximated by assuming fractional changes in specific humidity over land are equal to fractional change in the ocean source from which the land gets its moisture:

where γ = q v,L /q v,O . Repeating the same procedure as before, and assuming fixed relative humidity over the ocean moisture source plus fixed γ then gives:

and humidity is the primary driver wherever:
$$
q_{v, L} > \frac{A}{174\gamma}.
$$</p>

<p>The amplification factor A = ∆T L /∆T O ≈ ∆θ L /∆T O and is typically between 1 and 2 (<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2006gl028164">ref</a>), while a typical value of γ in climate model simulations is 0.7 (<a href="http://pog.mit.edu/src/byrne_land_relative_humidity_decrease_2016.pdf">ref</a>) so that A/γ ≈ 1.5-3. Hence the baseline specific humidity threshold may be several times higher over land than over ocean. (In the paper I also repeat this derivation to include changes in relative humidity.)</p>

<h3>CMIP6 analysis</h3>

<p>To investigate the relative importance of changes in temperature and in specific humidity for \(\theta_E\) changes, I looked at data from simulations with 14 CMIP6 models in which CO 2 concentrations were increased at 1%/year (these were the models with the required data when I did the analysis).</p>

<p>The multi-model composite of changes in 98th percentile \(\Delta\theta_E\) events clearly shows that changes in moisture are the primary driver of the pattern of changes in equivalent potential temperature  (compare panels a and c). For example, there are large increases in \(\Delta\theta_E\) over equatorial Africa, particularly along the coastline of the Bay of Guinea, and smaller increases over the Sahara, which match the pattern of specific humidity changes. By contrast, the potential temperature changes over Africa are much more uniform (panel b).</p>

<p>To quantify the relative contributions of temperature and moisture I calculated the ratio \(Q = L v ∆q v /c p ∆θ\). Over oceans there is close agreement with the theory, as the red contours in the next figure, which denote where \(Q = 1\), closely match the green contours, which show the 5.6gkg −1 isopleth again. Over land, \(Q \leq 1\) over desert regions, with a larger extent than predicted from the green contours, and is also less than one over much of Europeand central Asia, central Brazil and central India. Experimenting with other contour levels suggests that \(q_{v,0}\) varies over land between 5-10gkg −1 , with substantial regional variations. For example, the North Atlantic experiences the slowest warming of any region, while Europe warms at a similar rate to other land regions at the same latitude (Figure 1b). This results in a large amplification factor over Europe, so that temperature is the main driver of the \(\Delta\theta_E\) response even though the baseline specific humidity is relatively high, and \(q_{v,0}\) ≈ 9gkg −1 over Europe. By contrast, over Australia, southern Africa and the southern part of South America the \(Q = 1\) contours closely follow the \(q_{v,0}\) =5.6gkg −1 contours. These variations in \(q_{v,0}\) highlight the role of regional factors in determining the relative contributions of humidity and temperature to heat stress extremes over land.</p>

<p>Similar results were seen in individual models, and comparing seasonal (e.g., JJA) changes. Thus the much larger regional variation of \(\Delta q_v\) (compare panels b and c of Figure 2) dominates that \(\Delta\theta_E\), and the changes in \(\Delta\theta_E\) can be approximated as coming from a spatially-homogeneous distribution of potential temperature changes and a spatially-heterogeneous pattern of specific humidity changes:
$$
\Delta \theta_{E, 98}(x, y) \approx \theta_{E, 98}(x, y)\left(\frac{\Delta\theta_{98}}{\theta_{98}} + \frac{L}{c_pT_{98}}\Delta q_{v, 98} (x, y)\right),
$$
</p>


<h3>Implications</h3>

A lot more work is needed to understand and constrain changes in heat stress. For example, we need a better understanding of what controls relative humidity changes, particularly over mid-latitudes; how surface processes, like soil moisture feedbacks, affect local moisture levels; and how the dynamics of synoptic-scale weather events responsible for heat stress extremes change with warming. But I like to think that this result -- that specific humidity is the main driver of heat stress changes -- gives us a starting point for choosing what to focus on in future studies. At most locations, particularly over land, if we can understand how specific humidity changes with warming, it will tell us a lot about how heat stress changes with warming. 








