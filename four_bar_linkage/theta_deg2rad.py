import numpy as np


def conversion(theta_2: float, theta_3: float, theta_4: float) -> float:
    """Returns the four-bar linkage positions in radian."""

    theta_2_rad = np.deg2rad(theta_2)
    theta_3_rad = np.deg2rad(theta_3)
    theta_4_rad = np.deg2rad(theta_4)

    return theta_2_rad, theta_3_rad, theta_4_rad
