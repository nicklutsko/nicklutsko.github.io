---
layout: post
title: "Understanding the Regional Pattern of Surface Warming"
date: 2018-10-10
---

Among all the uncertainties about future climate change, one thing we do have confidence in is the pattern of surface warming. This is a very useful thing to know, for instance because we can use pattern scaling to get a good first-order estimate of regional warming: non-dimensionalizing the pattern by the change in global-mean surface temperature, local warming (T) = global-mean surface warming (T) x the pattern.  

As an example, this is a figure from a review paper by <a href="https://www.nature.com/articles/nclimate2689.pdf">Xie et al. (2015)</a> on improving predictions of regional climate changes, and shows the CMIP5 model-mean changes in surface temperature (top) and precipitation (bottom) under the RCP4.5 scenario between 2081-2100 and 1986-2005:

<img src="http://nicklutsko.github.io/notes/images/Xie_et_al_warming.png" alt="Xie et al. Fig 1" style="position:absolute; left:250px; width:310px;height:392px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

Hatching indicates that the changes aren't robust across models, in the sense of the models not all giving the same sign of response. This isn't a very stringent test, but it's enough to make a big difference between panel a, which doesn't have any hatching, and panel b, which has a lot of hatching. The pattern of warming is also pretty robust across emission scenarios and assumptions about climate sensitivity.

Looking at panel a, some large-scale features stand out:
<ul>
<li>The land warms more than the oceans</li>
<li>The largest warming is in the Arctic</li>
<li>There's less warming over Antarctica</li>
<li>The smallest warming is in the North Atlantic, just south of Greenland</li>
<li>There is enhanced warming over the equator</li>
<li>There's also reduced warming in the south-east Pacific, off the coast of Peru.</li>
</ul>

In addition to consistency across models, our confidence in the regional pattern of warming comes from having relatively good understandings of what causes these features. Xie et al go over some of these explanations, but I wanted to spell them out in more detail.

<h3>Greater warming over land than over the oceans</h3>

A first-order explanation for why land warms more than ocean comes from a kind of quasi-equilibrium theory. Assume temperatures over land and over the oceans are moist adiabatic: they follow dry adiabats up to the lifting condensation level (LCL), and then moist adiabats higher up. The LCL is lower over the oceans, since the air over the oceans is moister. Next, assume that temperatures over land are the same as over the oceans at the height of the land’s LCL. Working back down, the land surface is warmer because of the difference in lapse-rates between the heights of the ocean’s LCL and the land’s LCL. 

<img src="http://nicklutsko.github.io/notes/images/land_warming_example.png" alt="Land warming example" style="position:absolute; left:250px; width:266px;height:200px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

If the ocean surface warms, the moist adiabat over the ocean between these two heights is reduced, but the dry adiabatic lapse-rate over the land is fixed, creating a land-ocean contrast in warming. This is compounded by reductions in the relative humidity over land, which moves the LCL over land further up, further amplifying the difference in responses.

Some other important factors include differences in the responses of sensible and latent heat fluxes and differences in cloud cover changes. For instance, Joshi et al. (2008) suggest that reductions in relative humidity over land cause reductions in local cloud cover, which further amplify the land-ocean warming contrast. As with anything involving clouds however, this is a fairly uncertain mechanism.

Some references:
<a href="http://www.mit.edu/~pog/src/byrne_land_ocean_warming_contrast_2013.pdf">Byrne and O'Gorman (2013)</a> (and see follow-ups for similar theories for relative humidity differences)
<a href="https://link.springer.com/article/10.1007/s00382-007-0306-1">Joshi et al. (2008)</a> for similar theory and also discussion of clouds.

<h3>Arctic amplification of warming</h3>

Amplification of warming at high latitudes is seen in models ranging from highly idealized to comprehensive climate models. There are number of reasons for this, but first it’s worth noting that the forcing due to increasing CO2 is actually tropically-amplified, so in the absence of feedbacks there would be more warming in the tropics. Water vapor also promotes tropical amplification, because the water vapor feedback is largest there.

In idealized models, these are countered by the Planck feedback (by T^4 colder regions have to warm up more), increases in poleward energy transport and differences in the lapse-rate feedback, which is positive at high latitudes and negative at low latitudes.  In comprehensive models a major additional factor in Arctic amplification is reductions in albedo due to reductions in snow cover and sea-ice. It’s less clear how clouds, surface fluxes and ocean transport contribute to polar amplification, but their effects seem to be minor.

Some useful references:
<a href="https://www.nature.com/articles/ngeo2071.pdf">Pithan and Mauritsen (2014)</a> for a CMIP5 model perspective.
<a href="http://www.meteo.mcgill.ca/~tmerlis/publications/henry_linear_rad.pdf">Henry and Merlis</a>, and <a href="https://journals.ametsoc.org/doi/abs/10.1175/JCLI-D-18-0103.1">Lutsko and Popp (2018)</a>, for more idealized perspectives.
<a href="http://web.mit.edu/~twcronin/www/document/CroninJansen2015.pdf">Cronin and Jansen (2016)</a> for understanding lapse-rate changes

<h3>Relatively muted warming over Antarctica</h3>

So why does Antarctica warm up less? Since idealized models show polar amplification, the answer must be in effects that aren't included in models without continents, realistic oceans, etc.

The main factor is that the mid-latitude jet in the southern hemisphere tends to shift southwards in global warming simulations. This induces northwards Ekman flow in the Southern Ocean, which brings cool waters up to the surface around the Antarctic continent. These cold waters originally sank in the North Atlantic, so it takes centuries for them to “feel” the effects of climate change. Their presence also promotes sea-ice growth, which increases the albedo around Antarctica, while the northwards flow also advects extra energy taken up by the ocean to lower latitudes, away from the Antarctic continent.

In these ways, the Southern Ocean acts to insulate Antarctica from global warming. Cloud changes may also play a role in cooling the mid- to high-latitudes in the southern hemisphere, though this is less certain. 
Some references:
<a href="http://rsta.royalsocietypublishing.org/content/372/2019/20130040">Marshall et al. (2014)</a>
<a href="https://www.nature.com/articles/ngeo2731.pdf">Armour et al. (2016)</a>

<h3>Reduced warming over the North Atlantic</h3>

Reduced warming over the North Atlantic, or even a warming “hole”, is seen in observations as well as in simulations of future warming. There are a few different factors at play, and as far as I can tell the jury is still out on how much each of these contributes.

First, the reduced warming is often said to be caused by a slow down of the AMOC. So less heat is transported northwards into the surface waters of the North Atlantic, which cool as a result. Melting of the Greenland ice sheet could also play a role, as the cold, fresh run-off flows into the North Atlantic (though since climate models have fixed ice sheets they can’t capture this effect). Similarly, changes in ocean circulation cause increased flow into the North Atlantic from the Arctic Ocean and from the Labrodor Sea, which also leads to cooling. Both of these effects also act to shut off the convection in the North Atlantic. This effectively moves heat upwards by bringing cold water down, and so reduced convection leads to further cooling of the North Atlantic, as well as to a slowdown of the AMOC.

Some references:
<a href="http://www.realclimate.org/index.php/archives/2018/05/if-you-doubt-that-the-amoc-has-weakened-read-this/">Real Climate post</a>
<a href="https://journals.ametsoc.org/doi/10.1175/JCLI-D-17-0635.1">Gervais et al. (2018)</a>





<h3>Enhanced warming over the equator and reduced warming in the southeast Pacific</h3>

The enhanced equatorial warming is particularly noticeable in the Pacific ocean, and is mostly due to coupled atmosphere-ocean dynamics. As the tropical atmospheric circulation slows down, upwelling of cold water at the equator is reduced, inducing additional warming at the equator. Reduced evaporative cooling, because of near-surface increases in stability and relative humidity, may also play a role, though this seems to be less certain.

Coupled dynamics are also responsible for the slower warming over the southeast Pacific, through a wind-evaporation-SST (WES) feedback: an increase in surface wind speed increases evaporation, and this cools SSTs locally, which in turn further increases surface wind speeds. The WES feedback has already been identified as playing a role in ENSO dynamics, and experiments suggest that CO2 forcing causes an initial cooling of SSTs in the southeast Pacific, kicking off the WES cycle.

<a href="https://journals.ametsoc.org/doi/pdf/10.1175/2009JCLI3329.1">Xie et al (2010)</a> is a useful reference for both these features





