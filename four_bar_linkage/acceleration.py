import numpy as np
import theta_deg2rad as deg2rad


def angular_acceleration(a: float, b: float, c: float, theta_2: float, theta_3: float, theta_4: float,
                         omega_2: float, omega_3: float, omega_4: float, alpha_2: float) -> float:
    """Returns the angular accelerations alpha_3 and alpha_4."""

    theta_2_rad, theta_3_rad, theta_4_rad = deg2rad.conversion(theta_2, theta_3, theta_4)

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


def linear_acceleration(a: float, b: float, c: float, theta_2: float, theta_3: float, theta_4: float, omega_2: float, omega_3: float,
                        omega_4: float, alpha_2: float, alpha_3: float, alpha_4: float) -> float:
    """Returns the absolute and relative total linear accelerations."""

    theta_2_rad, theta_3_rad, theta_4_rad = deg2rad.conversion(theta_2, theta_3, theta_4)

    a_a = np.sqrt((-a*alpha_2*np.sin(theta_2) - a*omega_2**2*np.cos(theta_2))**2 + (a*alpha_2*np.cos(theta_2) - a*omega_2**2*np.sin(theta_2))**2)
    a_b = np.sqrt((-c*alpha_4*np.sin(theta_4) - c*omega_4**2*np.cos(theta_4))**2 + (c*alpha_4*np.cos(theta_4) - c*omega_4**2*np.sin(theta_4))**2)
    a_b_a = np.sqrt((-b*alpha_3*np.sin(theta_3) - b*omega_3**2*np.cos(theta_3))**2 + (b*alpha_3*np.cos(theta_3) - b*omega_3**2*np.sin(theta_3))**2)

    return a_a, a_b, a_b_a
