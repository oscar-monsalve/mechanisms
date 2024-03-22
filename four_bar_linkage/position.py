import numpy as np


def k_constants(a, b, c, d):
    """Returns the K_n constants. Its arguments are the mechanisms' lengths a, b, c, d."""

    k1 = d / a
    k2 = d / c
    k3 = (a**2 - b**2 + c**2 + d**2) / (2 * a * c)
    k4 = d / b
    k5 = (c**2 - d**2 - a**2 - b**2) / (2 * a * b)

    return k1, k2, k3, k4, k5


def A_constants(theta_2):
    """Returns the capital letters variables. It's arguments are theta_2."""

    theta_2_deg = np.deg2rad(theta_2)
    kn = k_constants()
    A = np.cos(theta_2_deg) - kn[0] - kn[1]*np.cos(theta_2_deg) + kn[2]
    B = -2 * np.sin(theta_2_deg)

    return A, B


# four-bar linkage data
theta_2 = 40  # degrees
a = 40
b = 120
c = 80
d = 100

print(k_constants(a, b, c, d))
