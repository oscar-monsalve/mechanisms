import numpy as np
import matplotlib.pyplot as plt
import position as pos
import grashof as grashof
import velocity as vel
import acceleration as accel


def main() -> None:

    # four-bar linkage data
    a: float = 40
    b: float = 120
    c: float = 80
    d: float = 100
    theta_2 = np.linspace(0, 360, 360)  # degrees
    omega_2: float = 25  # rad/s
    alpha_2: float = 5  # rad/s^2

    is_grashof = grashof.is_grashof(a, b, c, d)

    if is_grashof is True:

        while True:
            try:
                input_theta_2 = int(input("Enter the input link position in degrees (only integers): "))
                break
            except ValueError:
                print("Error. Enter a number. Try again...\n")

        # Position
        k1, k2, k3, k4, k5 = pos.k_constants(a, b, c, d)
        A, B, C, D, F, E = pos.A_constants(theta_2, k1, k2, k3, k4, k5)
        theta_3_1, theta_4_1, transmission_angle_open = pos.position_open(A, B, C, D, F, E)
        theta_3_2, theta_4_2, transmission_angle_crossed = pos.position_crossed(A, B, C, D, F, E)

        # Velocity
        omega_3_1, omega_4_1 = vel.angular_velocities(a, b, c, theta_2, theta_3_1, theta_4_1, omega_2)
        omega_3_2, omega_4_2 = vel.angular_velocities(a, b, c, theta_2, theta_3_2, theta_4_2, omega_2)
        v_a, v_b_a, v_b = vel.linear_velocities(a, b, c, omega_2, omega_3_1, omega_4_1)

        # Acceleration
        alpha_3_1, alpha_4_1 = accel.angular_acceleration(
            a, b, c, theta_2, theta_3_1, theta_4_1, omega_2, omega_3_1, omega_4_1, alpha_2
        )

        # Position print
        print("---------------------------------------")
        print("Position:")
        print("Open configuration:")
        print(f"Theta_3_1 is: {theta_3_1[input_theta_2]: .2f} °")
        print(f"Theta_4_1 is: {theta_4_1[input_theta_2]: .2f} °")
        print(f"The transmission angle is: {transmission_angle_open[input_theta_2]: .2f} °\n")

        print("Crossed configuration:")
        print(f"Theta_3_2 is: {theta_3_2[input_theta_2]: .2f} °")
        print(f"Theta_4_2 is: {theta_4_2[input_theta_2]: .2f} °")
        print(f"The transmission angle is: {transmission_angle_crossed[input_theta_2]: .2f} °")
        print("---------------------------------------\n")

        # Velocity print
        print("Velocity:")
        print("Open configuration:")
        print(f"Omega_3_1 is: {omega_3_1[input_theta_2]: .2f} rad/s")
        print(f"Omega_3_1: {omega_4_1[input_theta_2]: .2f} rad/s")
        print(f"V_A is: {v_a: .2f} length/s")
        print(f"V_B_A is: {v_b_a[input_theta_2]: .2f} length/s")
        print(f"V_B is: {v_b[input_theta_2]: .2f} length/s\n")

        print("crossed configuration:")
        print(f"omega_3_2 is: {omega_3_2[input_theta_2]: .2f} rad/s")
        print(f"omega_3_1 is: {omega_4_2[input_theta_2]: .2f} rad/s")
        print("---------------------------------------\n")

        # Acceleration print
        print("Acceleration:")
        print("Open configuration:")
        print(f"Alpha_3_1 is: {alpha_3_1[input_theta_2]: .2f} rad/s^2")
        print(f"Alpha_4_1: {alpha_4_1[input_theta_2]: .2f} rad/s^2")
        print("---------------------------------------\n")

        plt.plot(theta_2, theta_3_1)
        plt.plot(theta_2, theta_4_1)
        plt.plot(theta_2, transmission_angle_open)
        plt.legend([r"$\theta_3$", r"$\theta_4$", r"$\mu$"])
        plt.title("Four-bar linkage position (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Angular position (°)")
        plt.show()

    if is_grashof is False:
        print("Therefore, no link can describe a full rotation.")
        print("Please change the lengths of your linkages so the Grashof's law is satified")


if __name__ == "__main__":
    main()
