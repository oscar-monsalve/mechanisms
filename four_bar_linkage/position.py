import numpy as np


def check_grashof(a: float, b: float, c: float, d: float) -> bool:
    min_len = min(a, b, c, d)
    max_len = max(a, b, c, d)

def k_constants(a: float, b: float, c: float, d: float) -> float:
    """Returns the K_n constants. Its arguments are the mechanisms' lengths a, b, c, d."""

    k1 = d / a
    k2 = d / c
    k3 = (a**2 - b**2 + c**2 + d**2) / (2 * a * c)
    k4 = d / b
    k5 = (c**2 - d**2 - a**2 - b**2) / (2 * a * b)

    return k1, k2, k3, k4, k5


def A_constants(theta_2: float, k1, k2, k3, k4, k5) -> float:
    """Returns the capital letters variables. It's arguments are theta_2, k1, k2, k3, k4, k5"""

    theta_2_rad = np.deg2rad(theta_2)
    A = np.cos(theta_2_rad) - k1 - (k2 * np.cos(theta_2_rad)) + k3
    B = -2 * np.sin(theta_2_rad)
    C = k1 - (k2 + 1) * np.cos(theta_2_rad) + k3
    D = np.cos(theta_2_rad) - k1 + (k4 * np.cos(theta_2_rad)) + k5
    E = -2 * np.sin(theta_2_rad)
    F = k1 + (k4 - 1) * np.cos(theta_2_rad) + k5

    return A, B, C, D, E, F


def position_open(A, B, C, D, E, F):
    """Returns the position of the mechanism (theta_3_1 & theta_4_) for the open configuration"""

    theta_3_1 = 2 * np.arctan((-E - np.sqrt(E**2 - 4 * D * F)) / (2 * D))
    theta_4_1 = 2 * np.arctan((-B - np.sqrt(B**2 - 4 * A * C)) / (2 * A))
    transmission_angle = theta_4_1 - theta_3_1

    return np.rad2deg(theta_3_1), np.rad2deg(theta_4_1), np.rad2deg(transmission_angle)


def position_crossed(A, B, C, D, E, F):
    """Returns the position of the mechanism (theta_3_2 & theta_4_2) for the crossed configuration"""

    theta_3_2 = 2 * np.arctan((-E + np.sqrt(E**2 - 4 * D * F)) / (2 * D))
    theta_4_2 = 2 * np.arctan((-B + np.sqrt(B**2 - 4 * A * C)) / (2 * A))
    transmission_angle = theta_3_2 - theta_4_2

    return np.rad2deg(theta_3_2), np.rad2deg(theta_4_2), np.rad2deg(transmission_angle)
