# Mechanisms: theoretical analysis

This repository contains theoretical analysis for the position, velocity, and acceleration and jerk for
mechanisms as the four-bar linkage and cam mechanisms.


## theoretical analysis of the four-bar linkage

### Position

The position of the four-bar linkage is determined by the following equations:

$$\theta_{3_{1,2}} = 2\arctan\left( \frac{-E\pm \sqrt{E^2-4DF}}{2D}\right)$$

$$\theta_{4_{1,2}} = 2\arctan\left( \frac{-B\pm \sqrt{B^2-4AC}}{2A}\right)$$

where A, B, C, D, E, F are variables that depend on the crank position $(\theta_2)$ and some constants $K_n$:

| $A = \cos(\theta_2) - K_1 - K_2 \cos(\theta_2) + K_3$  | $K_1$
|                                                        |
| $B = -2\sin(\theta_2)$                                 |
|                                                        |
| $C = - K_1 - (K_2 + 1) \cos(\theta_2) + K_3$           |
|                                                        |
| $D = \cos(\theta_2) - K_1 + K_4 \cos(\theta_2) + K_5$  |
|                                                        |
| $E = -2\sin(\theta_2)$                                 |
|                                                        |
| $F = - K_1 + (K_4 + 1) \cos(\theta_2) + K_5$           |
