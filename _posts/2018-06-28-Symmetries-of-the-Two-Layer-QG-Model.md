---
layout: post
title: "The Two Climates of the Two-Layer QG Model"
date: 2018-06-28
use_math: true
---

<p>One of the simplest models of mid-latitudes dynamics is Phillips’ two-layer quasi-geostrophic $($QG$)$ model on a \beta plane. This consists of two layers of constant density, with the top layer lighter than the bottom layer, whose interface is relaxed to some equilibrium slope $($this represents the tropics receiving more solar radiation than high latitudes$)$. Surface friction is also added to the lower layer:</p>

<center><img src="http://nicklutsko.github.io/notes/images/2_layer_QG.jpg" alt="2_layer" style="width:483px;height:154px;" class="center"></center>

<p>The way to think about the dynamics of this system is that eddies try to flatten out the interface by transporting heat polewards, fighting against the radiative relaxation, and the equations for the two layers are:
$$
\frac{\partial q_k}{\partial t} + J(\psi_k, q_k) = &-\frac{1}{\tau_d}(-1)^k (\psi_1 - \psi_2 - \psi_R ) - \frac{1}{\tau_f}\delta_{k2}\nabla^2 \psi_k,
$$
where $q_k = \nabla^2 \psi_k + (-1)^k (\psi_1 - \psi_2) + \beta y$ is the potential vorticity, with $\psi$ the streamfunction and $\beta$ the gradient of the Coriolis parameter. $k$ = 1 for the top layer and 2 for the bottom layer, and the $\delta$-function indicates that the friction only acts in the lower layer. $\psi_R$ is the equilibrium slope which the interface is relaxed to, and is chosen to make the system baroclinically unstable.</p>

<p>This system was used by Phillips in 1958 as the basis for the first numerical weather model, and since then we’ve learned a lot about the atmosphere by studying the two-layer model because, despite its simplicity, it captures the main features of the mid-latitude circulation that we care about, like annular modes and the behavior of eddy-driven jets. $($Similar systems are used to study jets in the ocean and on other planets$)$.</p>

<h3>The Two Climates of the Model</h3>

<p>An important feature of the model’s climate is the fact that the PV gradient in the upper layer is larger in magnitude than the PV gradient in the lower layer:
$$
\frac{d\overline{q}_1}{dy} = \beta - \frac{d^2 \overline{u_1} }{dy^2} + \hat{u}, \\
\frac{d\overline{q}_2}{dy} = \beta - \frac{d^2 \overline{u_2} }{dy^2} - \hat{u}, 
$$
$($the main balance is between $\beta$ and the vertical wind shear$)$. The means that eddies can propagate further from their source in the upper layer than in the lower layer, which makes the dynamics of the upper layer more linear, with waves traveling far from their source. In the lower layer the waves essentially just form and break $($non-linearly$)$ in place $($see <a href="https://journals.ametsoc.org/doi/pdf/10.1175/JAS-D-17-0099.1">this paper</a> for more on lower layer eddies$)$.</p> 

<p>How can we switch this, so that the lower layer PV gradient is larger? One way is to reverse the temperature gradient so that the “pole” gets more sun than the “tropics”. This would be the case on a planet with high eccentricity, and in the two-layer model is done by reversing the sign  of $\psi_R$.This makes the PV gradient larger in the lower layer:


</p> 

<p>Another way to make the PV gradient larger in the lower layer is to take the original set-up and change the sign of $\beta$, i.e., $\beta → -\beta$. Everything stays the same except that the PV is now $q_k = \nabla^2 \psi_k + (-1)^k (\psi_1 - \psi_2) - \beta y$.</p>

<p>If we then make the co-ordinate transform $(x, y) → (-x, -y)$, we end up with exactly the same system as when reversing the temperature gradient:</p>

<p>So changing the sign of $\beta$ $($i.e., the sign of the rotation gradient$)$ and making the co-ordinate transform $(x, y) → (-x, -y)$ is exactly the same as reversing the temperature gradient. It turns out that this is also equivalent to moving the friction to the upper layer and switching the layers, i.e., making the co-ordinate transform $z → -z$:</p>

<p>In summary, the two-layer model has two climate: the Earth-like climate 1, and climate 2 which is like a planet with a reversed temperature gradient. We can go from climate 1 to climate 2 by making one of the perturbations discussed above, and can go back by making another perturbation $($and so on$)$:</p>

<center><img src="http://nicklutsko.github.io/notes/images/relationships.png" alt="relationships" style="width:400px;height:100px;" class="center"></center>

<p>The key difference between the two climates is that in climate 1 the friction is in the layer with the smaller PV gradient, while in climate 2 the friction is in the layer with the larger PV gradient.</p>

<h3>Simulating the Climates</h3>

<p>Here’s what the zonal-mean winds look like in simulations of these climates with Earth-like parameters:</p>

<center><img src="http://nicklutsko.github.io/notes/images/climate_comp_2.png" alt="climate_comp" style="width:400px;height:400px;" class="center"></center>

<p>and here’s snapshots of the PV in both layers of an Earth-like simulation and a simulation with reversed temperature gradient:</p>

<center><img src="http://nicklutsko.github.io/notes/images/PV_snapshot.png" alt="PV_snapshot" style="width:450px;height:300px;" class="center"></center>

<p>Taking things further, these two climate are actually end-members of a continuum of climates; it is actually the ratio of the friction in the two-layers which matters. We can define a quantity $\Delta$, which is equal to the friction in layer 2 minus the friction in layer 1, divided by the friction in layer 2:</p>

<p>and you can smoothly go from climate 1 to climate 2 by varying $\Delta$ from -1 to 1:</p>

<center><img src="http://nicklutsko.github.io/notes/images/delta_comp.png" alt="delta_comp" style="width:400px;height:292px;" class="center"></center>

<p>To make things slightly more realistic, here are some simulations with the Held-Suarez model of a control Earth-like set-up $($top$)$, a set-up with a reversed temperature gradient $($middle$)$ and a set-up with a reversed temperature gradient and friction in the upper troposphere $($bottom$)$</p>

<center><img src="http://nicklutsko.github.io/notes/images/dycore_emfs.png" alt="dycore_emfs" style="width:400px;height:400px;" class="center"></center>

<p>The spherical geometry and presence of a stratosphere means things aren’t exact anymore, but qualitatively these climates are similar to the corresponding two-layer simulations.</p>

<h3>Examples of Climate 2</h3>

<p>There are some situations in which climate 2 could be relevant, such as a planet with high obliquity, or a situation with a strong negative topographic $\beta$ effect. Climate 2 might also arise in a situation with surface ice over the ocean inducing a strong drag at the top of the ocean.</p>

<p>I think the more interesting point about these results is that they highlight that the climate of the 2-layer system is defined by the the position of the friction relative to the PV gradients. We can change parameter values, but as long as the friction is in the layer with the smaller PV gradient the climate will be Earth-like.</p>

<p>$($Email me if you want code for any of the simulations$)$.</p>











