---
layout: post
title: "The Pattern Effect and Changing Climate Sensitivity Over the Historical Record"
date: 2018-12-16
use_math: true
---

<p>The best constraint we have on climate sensitivity is the historical record. Intuitively, it seems like we should be able to use this to say something about Earth's climate sensitivity, but this turns out to be pretty subtle.</p>

<p>One issue which has gotten attention recently is that the inferred climate sensitivity changes over time:

<img src="http://nicklutsko.github.io/notes/images/changing_sensitivity.png" alt="Changing Sensitivity" style="position:absolute; left:250px; width:468px;height:321px;" class="center">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
<p>$($From Andrews et al. (2018); $\lambda$ calculated for simulations of the historical record with eight different climate models. $\lambda$ is calculated by regressing $R$ against $T$ over sliding 30 year windows.$)$</p>

<p>The climate feedback parameter $\lambda$ was small between about 1920 and 1960 $($implying a high climate sensitivity$)$ and has been increasing since then $($implying a lower sensitivity$)$. To calculate this, an assumption is made about the forcing, $F$, and then the global-mean surface temperature $($$T$$)$ is regressed against the net TOA flux $R$, using $R = F - \lambda T$. Alternatively, you can also calculate $\lambda$ directly as the derivative $\partial R / \partial T$. Either way, observations and models give a consistent picture of $\lambda$ changing over the historical record.</p>

<h3>Explaining this with the Pattern Effect</h3>

<p>A major reason for this is the "pattern effect": the diagnosed feedback is sensitive to the pattern of warming. So the strength of $\lambda$ changes over time as SST patterns change over time.</p> 

<p>To understand this, consider a two box model of Earth's climate, with energy transport parameterized based on the temperature difference between the two boxes. The TOA radiation budget for this system can be written as</p>
\begin{align}
\begin{bmatrix}
    R_1 \\
    R_2
\end{bmatrix}
=
\begin{bmatrix}
    \lambda_1 - c & +c\\
    +c  &\lambda_2 - c
\end{bmatrix}
\begin{bmatrix}
    T_1 \\
    T_2
\end{bmatrix}
+
\begin{bmatrix}
    F_1 \\
    F_2
\end{bmatrix}
+
\begin{bmatrix}
    F_{r, 1} \\
    F_{r, 2}
\end{bmatrix},
\end{align}
<p>where $T_i$ is the temperature in box $i$, $\lambda_i$ is the local radiative feedback in box $i$, $F_i$ is the CO$_2$ forcing in box $i$, $F_{r, i}$ is the non-CO$_2$ forcing in box $i$ and $c$ is the anomalous heat transport between the two boxes. We can write this using matrix notation as</p>
\begin{align}
\begin{bmatrix}
    R_1 \\
    R_2
\end{bmatrix}
=
\Lambda
\begin{bmatrix}
    T_1 \\
    T_2
\end{bmatrix}
+
\begin{bmatrix}
    F_1 \\
    F_2
\end{bmatrix}.
\end{align}
<p>This can then be divided up into the component due to the CO$_2$ forcing $($subscript $F$$)$ and a residual, which includes internal variability, aerosols, etc. $($subscript $r$$)$</p>
\begin{align}
\begin{bmatrix}
    R_{F, 1} \\
    R_{F, 2}
\end{bmatrix}
+
\begin{bmatrix}
    R_{r, 1} \\
    R_{r, 2}
\end{bmatrix}
=
\Lambda
\begin{bmatrix}
    T_{F, 1} \\
    T_{F, 2}
\end{bmatrix}
+
\begin{bmatrix}
    F_1 \\
    F_2
\end{bmatrix}
+
\Lambda
\begin{bmatrix}
    T_{r, 1} \\
    T_{r, 2}
\end{bmatrix}.
\end{align}
<p>For simplicity, I'm assuming that $\Lambda$ doesn't change over time and that the local feedbacks are the same for the forced component and the residual. To make things even easier, I'm also taking out the residual forcing, so there's just internal variability. In this system, changes in the climate sensitivity are entirely due to changes in the pattern of warming, since the $\Lambda$'s are constant over time and don't change for different forcings.</p>

<p>The inferred, ``true" global-mean feedback parameter in this system is 
$\lambda_g = \left$($\sum\Lambda \begin{bmatrix}
    T_{F, 1} \\
    T_{F, 2}
\end{bmatrix}\right$)$ / $($T_{F, 1} + T_{F, 2}$)$$
So, even if nothing else was going on, the global-mean climate sensitivity would change over time as $T_{F, 1}$ and $T_{F, 2}$ changed. If box 1 had a high sensitivity $($small $\lambda_1$$)$ and box 2 had a low sensitivity $($large $\lambda_2$$)$ but for some reason box 2 warmed up faster than box 1, then the observed climate sensitivity would evolve from being small to large as the warming in box 1 caught up.</p> Differences in ocean heat uptake could be create this evolution.

<p>With the residual, the effective climate sensitivity becomes</p>
$\lambda_g = \left$($\sum\Lambda \begin{bmatrix}
    T_{F, 1} + T_{r, 1} \\
    T_{F, 2} + T_{r, 2}
\end{bmatrix}\right$)$ / $($T_{F, 1} + T_{F, 2} + T_{r, 1} + T_{r, 2}$)$$
<p>So the residual temperature patterns -- here just made up of internal variability -- could cause large changes in the inferred climate sensitivity.</p>

<p>In summary, even though the local feedbacks are constant, the inferred global-mean feedback parameter will change over time both because the pattern of the forced response changes and because of internal variability. In equilibrium, the global-mean feedback is</p> 
$\lambda_{e, g} = \left$($\sum\Lambda \begin{bmatrix}
    T_{e, F, 1} \\
    T_{e, F, 2}
\end{bmatrix}\right$)$ / $($T_{e, F, 1} + T_{e, F, 2}$)$$
<p>where the subscript $e$ denotes an equilibrium quantity. So even if we know $\lambda_g$ and $\Lambda$ at some point in time, we don't know the equilibrium climate sensitivity because we don't know the equilibrated temperature response $T_e$; we'd just have $T$, which is a transient response.</p>

<p>Even in this simple model, the pattern effect makes it hard to estimate Earth's sensitivity from the historical record. In the real world, there's also the residual forcings of aerosols, volcanoes, etc.; the possibility that the local feedbacks change over time; the possibility of non-local feedbacks; and ocean heat uptake, which I've mostly ignored here. All of this can cause the sensitivity we diagnose from observations over the 100 years to vary widely.</p> 













