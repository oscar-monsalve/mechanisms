import numpy as np
import theta_deg2rad as deg2rad


def angular_velocities(a: float, b: float, c: float, theta_2: float, theta_3: float, theta_4: float, omega_2: float) -> float:
    """
    Returns the angular velocities omega_3 and omega_4. The arguments are the lengths a, b,c, the position theta_2, theta_3, theta_4, and
    the angular velocity omega_2.
    """

    theta_2_rad, theta_3_rad, theta_4_rad = deg2rad.conversion(theta_2, theta_3, theta_4)

    omega_3 = (a * omega_2 * np.sin(theta_4_rad - theta_2_rad)) / (b * np.sin(theta_3_rad - theta_4_rad))
    omega_4 = (a * omega_2 * np.sin(theta_2_rad - theta_3_rad)) / (c * np.sin(theta_4_rad - theta_3_rad))

    return omega_3, omega_4


def linear_velocities(a: float, b: float, c: float, omega_2: float, omega_3: float, omega_4: float) -> float:
    """Returns the linear velocities v_a, v_b, and v_b_a"""
    v_a = a * omega_2
    v_b_a = b * omega_3
    v_b = c * omega_4

    return np.abs(v_a), np.abs(v_b_a), np.abs(v_b)
