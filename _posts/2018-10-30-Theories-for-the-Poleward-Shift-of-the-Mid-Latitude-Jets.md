---
layout: post
title: "Theories for the Poleward Shifts of the Mid-Latitude Jets"
date: 2018-10-30
use_math: true
---

<p>A major open problem in atmospheric dynamics is what causes the eddy-driven mid-latitude jets to shift polewards under climate change and, conversely, to shift equatorwards during strong El Nino events. This is seen in idealized models and in comprehensive climate model simulations of future warming scenarios, though more clearly in the southern hemisphere than in the northern hemisphere $($where there’s more land$)$. Understanding these shifts is important scientifically and for society, especially as they affect the location and severity of extreme mid-latitude weather events.</p>

<p>A closely related question is what causes the tropical circulation to widen and contract in these scenarios $($see <a href="https://www.nature.com/articles/s41558-018-0246-2.pdf">here</a> for a recent review$)$. These two phenomena might be related, but I’m not going to get into that here, and only focus on the jet shifts.</p>

<p>There are several different theories for why jets shift, but no consensus. To put these together I find it useful to use this schematic of dynamics of the mid-latitude upper troposphere:

<img src="http://nicklutsko.github.io/notes/images/jet_schematic.png" alt="jet schematic" style="position:absolute; left:250px; width:450px;height:283px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

This is the classic picture of a baroclinically unstable source region – the jet – where eddies are excited and then propagate away. The eddies break at lower and higher latitudes and flux momentum back into the jet. With this picture, jets could shift because of shifts of the source region or of the sink regions, which affect the eddy momentum fluxes that drive the jet.</p>

<h3>Background: the zonal-mean structure of global warming</h3>

<p>The jets feel the effect of global warming through the structure of the temperature response in height and latitude. The latitudinal variations in the response are particularly important, since the zonal wind is connected to the meridional temperature gradient by the thermal wind relation:
$$
\frac{\partial u}{\partial z} \sim \frac{\partial T}{\partial y}
$$
<p>With global warming the largest warming is in the tropical upper troposphere and, in northern hemisphere winter, in the high-latitude lower troposphere:</p>

<img src="http://nicklutsko.github.io/notes/images/warming_pattern.png" alt="warming pattern" style="position:absolute; left:300px; width:354px;height:145px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br />

<p>$($Figure 6 from <a href="https://ore.exeter.ac.uk/repository/bitstream/handle/10871/19116/globwarm.pdf?sequence=1&isAllowed=y">Vallis et al. $($2015$)$</a>. Sorry for the jet colormap.$)$</p>

<p>So the meridional temperature gradient in the upper troposphere increases and we expect the mean winds to accelerate in the upper troposphere/lower stratosphere. In the lower troposphere the meridional temperature gradient is reduced, resulting in a weakening of low level baroclinicity. During El Nino events there is also enhanced warming of the tropical upper troposphere, but over a narrower range of latitudes, and this difference is probably key to the opposing responses of the jet.</p>


<h3>Moving the sinks</h3>

<p>The dispersion relation for a Rossby wave is:
$$
c =  u - \frac{\beta}{K^2}
$$
with $u$ the zonal-mean zonal wind, $c$ the phase speed of the wave, $\beta$ the meridional gradient of the Coriolis parameter and $K$ the total wavenumber. Rossby waves break at their critical latitudes, where $u \sim c$ and $K$ goes to infinity $($these are also called critical layers$)$. So shifts of the sink regions are due to some combination of changes in the waves' phase speeds and changes in the zonal-mean wind.</p>

<ul>
<li><a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007GL031200">Chen and Held $($2007$)$</a> $($see also <a href="https://journals.ametsoc.org/doi/full/10.1175/2008JCLI2306.1">Chen et al. $($2008$)$</a>$)$ focus on the breaking region on the equatorward side of the jet. This seems like a good starting point because Earth's spherical geometry means that eddies preferentially propagate equatorward, and the largest eddy momentum fluxes are on this side of the jet.
<br /><br />
Chen and Held make a relatively simple argument: because the subtropical winds accelerate, the equatorward critical layer $($where $u = c$$)$ moves polewards, so waves break closer to the jet. This effectively shifts the eddy momentum fluxes into the jet polewards and the jet shifts as well. </li>
<br />
<li><a href="https://journals.ametsoc.org/doi/pdf/10.1175/2010JCLI3738">Kidston et al. $($2010$)$</a> make an argument based on changes to eddies’ phase speeds. They focus on the $K$ term in the dispersion relation and suggest that, as a result of global warming, eddies get larger $($$K$ gets smaller$)$. If eddies’ size is set by the first baroclinic Rossby radius:
$$
\lambda_R = \frac{NH}{f}
$$
with $N$ the static stability, $H$ the height of the tropopause and $f$ the coriolis parameter; then since the tropopause rises under global warming $($see the Vallis et al. paper for an explanation of why this happens$)$, $\lambda_R$ increases and, equivalently, $K$ decreases. This slows down the eddies’ phase speeds, so eddies actually break further from the jet.
<br /><br />
Kidston et al. then point out that the sink region on the poleward side of the jet overlaps with the source region. Since eddies are able to propagate further in a warmer world, they break further from the jet and this overlap is reduced. So the eddy momentum fluxes increase on the poleward side of the jet, which is pushed poleward.
<br /><br />
This might seem to contradict the Chen mechanism, but Kidston et al. argue that both can be true at the same time. The acceleration of the subtropical winds could cause the critical layer on the equatorward side of the jet to move polewards, while at the same time the deceleration of the eddies could cause the poleward critical layer to move to higher latitudes, so both sinks shift poleward.</li>
<br />
<li>Related to the idea of eddy length-scales mattering, <a href="https://journals.ametsoc.org/doi/10.1175/2011JAS3641.1">Riviere $($2011$)$</a> focused on the nature of the individual eddies. Eddies which break anti-cyclonically tend to propagate equatorward, producing a poleward eddy momentum flux, while eddies which break cyclonically tend to propagate polewards and flux momentum towards the equator. Since long-wavelength eddies are more likely to break anti-cyclonically, an increase in eddy length-scales could increase anti-cyclonic wave-breaking, which would result in a poleward movement of the jet.</li>
<br />
<li>A different perspective is to focus on wave reflection. This happens when $\beta / K^2$ is larger than $u$ and so $c$ changes sign. Several studies suggested than in a warmer world, particularly because the mid-latitude jet speeds up, there is increased wave reflection on the poleward side of the jet (see <a href="https://journals.ametsoc.org/doi/10.1175/JAS-D-11-0188.1">Simpson et al. $($2012$)$</a> and <a href="https://journals.ametsoc.org/doi/abs/10.1175/JAS-D-11-0300.1">Kidston and Vallis $($2012$)$</a>). This means there are more equatorward propagating waves and a larger net poleward momentum flux across the jet.</li>
</ul>



<h3>Moving the source region</h3>

<p>The other approach is to focus on the baroclinic stirring which is the source for the eddies. The essence is that enhanced warming in the tropical troposphere results in a poleward shift of the maximum meridional temperature gradient at high altitudes which, combined with an increase in the static stability of the subtropics (<a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007GL031115">see here</a>), pushes the region of maximum baroclinicity polewards. A number of papers have attributed the poleward shift to this movement of the baroclinicity, including: <a href="https://journals.ametsoc.org/doi/10.1175/2011JAS3641.1">Lu et al. $($2008$)$</a>;  <a href="https://journals.ametsoc.org/doi/10.1175/2011JAS3641.1">Butler et al. $($2010$)$</a>;  <a href="https://link.springer.com/article/10.1007/s00382-010-0776-4">Wu et al. $($2011$)$</a>; and <a href="https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-12-00598.1">Tandon et al. $($2013$)$</a>. 

<h3>Teasing out the different mechanisms</h3>

<p>All of these mechanisms probably play a role in the jet shifts, with different levels of importance. And their relative importances probably vary across models of different complexity. Figuring out which mechanisms are most responsible for driving the shift isn't easy though. For instance, <a href="https://journals.ametsoc.org/doi/abs/10.1175/1520-0469%282000%29057%3C0415%3AABMFTE%3E2.0.CO%3B2">Robinson $($2000$)$</a> showed how an initial jet shift can cause a shift of the low-level baroclinicity, which feeds back on the jet shift. <a href="https://journals.ametsoc.org/doi/abs/10.1175/1520-0469%282000%29057%3C0415%3AABMFTE%3E2.0.CO%3B2">Barnes and Hartmann $($2011$)$</a> suggest that the poleward jet shift itself actually causes eddy length-scales to increase. Nevertheless, some attempts have been made to separate out the different effects:</p>

<ul>
<li><a href="https://journals.ametsoc.org/doi/10.1175/JAS-D-13-0200.1">David Lorenz</a> used a technique called Rossby wave chromatography to track how individual wavenumbers behave. This let him look at how different eddies influence the jet $($though not at changes in the stirring$)$, and Lorenz found that increased reflection is the key factor in the jet shift, though these results come from a barotropic model in which the stirring is prescribed.</li>
<br />
<li>Another approach was taken in a series of papers by Gang Chen, Jian Lu and co-authors $($e.g., <a href="https://journals.ametsoc.org/doi/abs/10.1175/JAS-D-12-0298.1">here</a>, <a href="https://link.springer.com/article/10.1007%2Fs00382-016-3092-9">here</a> and <a href="https://journals.ametsoc.org/doi/10.1175/JAS-D-16-0047.1">here</a>$)$, who looked at the responses of the jet to global warming-like perturbations across a large number of transient simulations with different models. These seem to consistently show that shifts of the baroclinic generation zone lag jet-shifts. This implies that the direct cause of jet shifts is shifts of the sink regions, though exactly how this comes about seems to be model-dependent.</li>
</ul>

<p>More than anything, what we need is a quantitative theory for the baroclinic stirring: what sets the strength and location of the source region. We might expect this to shift poleward because of changing temperature gradients, but we can't predict how changes in jet speeds and eddy properties will affect this, and are forced to rely on model simulations.</p> 

<p>Another issue is that these theories are all based on dry dynamics. To fully understand – and predict – the jet shifts we also need to understand the roles of water vapor and clouds $($<a href="https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-15-0394.1">Ceppi and Hartmann $($2016$)$</a> is an example of a study looking at the role of clouds$)$. The stratosphere also influences the jets, and it seems like the recovery of the ozone hole will push the southern hemispheric jet equatorward a bit over the next few decades. Finally, there's the problem of internal variability: how long it takes for jet shifts to be clearly discernible from the noise $($if they ever are$)$, and whether the jets' internal variability can be leveraged to predict how the jets will shift, using ideas like the <a href="https://journals.ametsoc.org/doi/10.1175/JAS-D-14-0356.1">Fluctuation-Dissipation Theorem</a>.</p> 










