---
layout: post
title: "Are Equilibrium Climate Sensitivity and Precipitation Sensitivity Inversely Related?"
date: 2019-05-29
---


<p>Equilibrium climate sensitivity (ECS) is the equilibrated warming of global-mean surface temperature in response to a doubling of CO\(_2\) concentrations. This important number is still quite uncertain, with a typical "likely" range being 2-4.5\(^\circ\)C. At the same time, we know that global-mean precipitation P increases by 1-3%\(^\circ\)C\(^{-1}\): if ECS = 4\(^\circ\)C, P increases by 4 - 12% after a doubling of CO\(_2\). So the precipitation sensitivity is the percentage increase in global-mean precipitation per degree of global warming.</p>

<p>Recently, <a href="https://www.nature.com/articles/s41558-018-0272-0">Watanabe et al. (2018) </a> suggested that there is an inverse relationship between ECS and precipitation sensitivity: models with a larger ECS should have smaller fractional changes in precipitation, and vice versa. Their reasoning is that low clouds -- which are the largest source of uncertainty in ECS -- have the opposite effect on the warming of surface temperature as they do on precipitation.</p>

<h3>The TOA energy budget</h3>

<p>To understand this, let's think about the top-of-atmosphere (TOA) radiation budget and the atmospheric radiation budget. We can write a (linearized) version of the TOA budget as
$$
R = F - \lambda T
$$
where \(R\) is the anomalous TOA radiative flux (positive for flux out of the system), \(F\) is some radiative forcing, like an increase in CO\(_2\) concentrations, \(\lambda\) is a radiative restoring co-efficient and \(T\) is the anomalous global-mean surface temperature. After a doubling of CO\(_2\) concentrations this system equilibrates so that
$$
T_{eq} = ECS = F / \lambda.
$$ 
Most of the uncertainty in ECS comes from the feedback parameter \(\lambda\), which is itself a sum of partial derivatives:
$$
\lambda = -\sum_i\frac{\partial R}{\partial X_i}\frac{\partial X_i}{\partial T},
$$
with one of the \(X_i\)'s being clouds:
$$
\lambda_C = -\frac{\partial R}{\partial C}\frac{\partial C}{\partial T}.
$$
where \(C\) is cloud cover. \(\lambda_C\) is the largest source of uncertainty in \(\lambda\), and hence in ECS, and most of this uncertainty comes from low clouds, whether these increase or decrease with warming.</p>

<p>From the TOA perspective the main effect of low clouds is to reflect solar radiation, increasing R and so \(\frac{\partial R}{\partial C} > 0\). If low cloud cover is reduced in a warmer world (\(\frac{\partial C}{\partial T}  &lt 0\)) then clouds act as a positive feedback on warming (\(\lambda_C\)  > 0), whereas clouds are a negative feedback if low cloud cover increases with warming.</p>

<h3>The Atmospheric Energy Budget</h3>

<p>The atmospheric energy budget can be written as:
$$
LWC = LH + SH + SWA,
$$
where \(LWC\) is the long-wave cooling of the atmosphere to space and to the surface, \(LH\) and \(SH\) are the latent and sensible heat fluxes, and \(SWA\)  is absorption of short-wave radiation by the atmosphere. The latent heat flux is approximately equal to \(LP\), where \(L\) is the latent heat of vaporization of water. The change in precipitation is then roughly:
$$
\Delta P \approx (\Delta LWC - \Delta SWA) / L = \Delta Q / L,
$$
as changes in the sensible heat flux are small, and with \(\Delta Q\) the net radiative cooling of the atmosphere.</p>

<p>Setting aside clouds for a moment, both \(LWC\) and \(SWA\) increase with warming, as a warmer atmosphere emits more longwave radiation and a moister atmosphere absorbs more shortwave radiation. In the net, the increased longwave cooling wins out, and precipitation increases.</p> 

<p>(Note: it's not obvious why it works out this way -- why the cooling increases faster than the absorption --, but see <a href="https://www.pnas.org/content/pnas/early/2018/10/16/1720683115.full.pdf?versioned=true">Jeevanjee and Romps (2018)</a> for an for an intuitive explanation for why we should expect this.)</p>

<p>Low clouds reflect incoming solar radiation, absorb upward longwave radiation emitted by the surface and emit long-wave radiation both upwards to space and downwards to the surface. Since these clouds emit at roughly the same temperature as the surface, the longwave radiation they absorb is roughly cancelled by their emission to space. The reflects short-wave doesn't affect \(SWA\) much, so in the net the most important effect of low clouds is to increase the atmosphere's longwave emission to the surface, increasing \(LWC\). Hence the change in atmospheric radiative cooling due to a change in low clouds is greater than zero:
$$
\eta_C = \frac{\partial LWC}{\partial C} > 0,
$$
and a reduction in low cloud cover with warming leads to a reduction in precipitation:
$$
P \approx (Q_{clear} + \eta_C\frac{\partial C}{\partial T_s}) / L.
$$</p>

<p> Thus low clouds have the opposite effect on precipitation as on warming: a decrease in low clouds leads to a decrease in precipitation, and vice-versa.</p>

<h3>Is there an inverse relationsip?</h3>

<p>If low clouds are the main source of uncertainty in ECS and in precipitation sensitivity, then this argument says that ECS and precipitation sensitivity should be inversely related in models: a model with a large reduction in low clouds under warming will have a high ECS and a low precipitation efficiency.</p> 

<p>Watanabe et al looked into this using a set of model ensembles. First, they did an ensemble of simulations with the MIROC5 model in which they multiplied the surface latent heat flux (the evaporation) by a fraction \(\beta\). Increasing \(\beta\) increases the ECS and decreases precipitation sensitivity, giving them exactly the relationship they were looking for (\(r \< \)-0.9).</p>

<p>(Note, it's unclear to me why \(\beta\) has this effect. One guess is that larger surface latent heat fluxes enhance subcloud turbulence, which promotes stratocumulus break-up, as in <a href="https://www.nature.com/articles/s41561-019-0310-1.pdf">Schneider et al (2019)</a>).</p>

<p>Next, Watanabe et al compared the sensitivities across a perturbed physics ensemble with MIROC5, in which 10 different parameters, mostly related to the convection scheme, were varied. The correlation is not so strong in this set of experiments, but they still found a correlation (\(r\) = -0.58. Finally, they looked at the CMIP5 data, where they only got a correlation (\(r\) = -0.2.</p>

<img src="http://nicklutsko.github.io/notes/images/Watanabe_fig.png" alt="Watanabe scatter" style="position:absolute; left:200px; width:411px;height:372px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
<p>(Figure 2b from Watanabe et al.)</p>


<p>So this argument seems to work in a single model with varied parameters, but doesn't work across models. This is probably because low clouds aren't the most important source of uncertainty in precipitation sensitivity across models, or at least because other factors are also important. For instance, <a href="https://www.nature.com/articles/nature15770">DeAngelis et al (2015)</a> showed that there is a strong relationship across models between precipitation sensitivity and the sensitivity of clear-sky short-wave absorption to warming. I.e., \(\partial SWA_{cl} / \partial T\) is responsible for a lot of the spread:</p>

<img src="http://nicklutsko.github.io/notes/images/DeAngelis_fig.png" alt="DeAngelis scatter" style="position:absolute; left:230px; width:327px;height:297px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
<p>(Figure 2b from Watanabe et al.)</p>


<p>Much of this spread comes from models using different radiation schemes, especially using bad radiation schemes. So potentially the spread due to shortwave absorption could be reduced, which might lead to a clearer inverse relationship between ECS and precipitation sensitivity. It will be interesting to check this once the data from the CMIP6 models is available.</p>
















