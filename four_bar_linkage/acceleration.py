import numpy as np


def angular_acceleration(a: float, b: float, c: float, theta_2: float, theta_3: float, theta_4: float,
                         omega_2: float, omega_3: float, omega_4: float, alpha_2: float) -> float:
    """Returns the angular accelerations alpha_3 and alpha_4."""

    theta_2_rad = np.deg2rad(theta_2)
    theta_3_rad = np.deg2rad(theta_3)
    theta_4_rad = np.deg2rad(theta_4)

    A = c * np.sin(theta_4_rad)
    B = b * np.sin(theta_3_rad)
    C = (
        a * alpha_2 * np.sin(theta_2_rad) + a * omega_2 ** 2 * np.cos(theta_2_rad) + b * omega_3 ** 2 *
        np.cos(theta_3_rad) - (c * omega_4 ** 2 * np.cos(theta_4_rad))
    )
    D = c * np.cos(theta_4_rad)
    E = b * np.cos(theta_3_rad)
    F = (
        a * alpha_2 * np.cos(theta_2_rad) - a * omega_2 ** 2 * np.sin(theta_2_rad) - b * omega_3 ** 2 *
        np.sin(theta_3_rad) + (c * omega_4 ** 2 * np.sin(theta_4_rad))
    )

    alpha_3 = (C * D - A * F) / (A * E - B * D)
    alpha_4 = (C * E - B * F) / (A * E - B * D)

    return alpha_3, alpha_4
