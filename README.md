# Mechanisms: theoretical analysis

This repository contains theoretical analysis for the position, velocity, and acceleration and jerk for
mechanisms as the four-bar linkage and cam mechanisms.


## theoretical analysis of the four-bar linkage

### Position

The position of the four-bar linkage is determined by the following equations:

$$\theta_{3_{1,2}} = 2\arctan\left( \frac{-E\pm \sqrt{E^2-4DF}}{2D}\right)$$

$$\theta_{4_{1,2}} = 2\arctan\left( \frac{-B\pm \sqrt{B^2-4AC}}{2A}\right)$$

where the subindices "1,2" refer to the open ("-") and crossed ("+") mechanism, respectively. A, B, C, D, E, F
are variables that depend on the input link position $(\theta_2)$ and some constants $K_n$:

| $A = \cos(\theta_2) - K_1 - K_2 \cos(\theta_2) + K_3$ | $K_1 = \frac{d}{a}$                       |
|:------------------------------------------------------|:------------------------------------------|
| $B = -2\sin(\theta_2)$                                | $K_2 = \frac{d}{c}$                       |
| $C = - K_1 - (K_2 + 1) \cos(\theta_2) + K_3$          | $K_3 = \frac{a^2 - b^2 + c^2 + d^2}{2ac}$ |
| $D = \cos(\theta_2) - K_1 + K_4 \cos(\theta_2) + K_5$ | $K_4 = \frac{d}{b}$                       |
| $E = -2\sin(\theta_2)$                                | $K_5 = \frac{c^2 - d^2 + a^2 + b^2}{2ab}$ |
| $F = - K_1 + (K_4 + 1) \cos(\theta_2) + K_5$          |                                           |

where $a, b, c, d$ are the lengths of the input, coupler, output, and fixed links, respectively.

The transmission angle $\mu$ is determined as:

$$\mu = \theta_4 - \theta_3$$
