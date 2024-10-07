import numpy as np
import matplotlib.pyplot as plt
import position as pos
import grashof as grashof
import velocity as vel
import acceleration as accel
import scienceplots
plt.style.use(["science", "notebook", "grid"])


def main() -> None:

    # four-bar linkage data
    a: float = 26
    b: float = 86
    c: float = 49
    d: float = 98
    theta_2 = np.linspace(0, 360, 360)  # degrees
    omega_2: float = 26  # rad/s
    alpha_2: float = omega_2 / 2  # rad/s^2

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
        v_a, v_b_a_1, v_b_1 = vel.linear_velocities(a, b, c, omega_2, omega_3_1, omega_4_1)
        v_a, v_b_a_2, v_b_2 = vel.linear_velocities(a, b, c, omega_2, omega_3_2, omega_4_2)

        # Acceleration
        alpha_3_1, alpha_4_1 = accel.angular_acceleration(a, b, c, theta_2, theta_3_1, theta_4_1, omega_2, omega_3_1, omega_4_1, alpha_2)
        alpha_3_2, alpha_4_2 = accel.angular_acceleration(a, b, c, theta_2, theta_3_2, theta_4_2, omega_2, omega_3_2, omega_4_2, alpha_2)
        a_a_1, a_b_1, a_b_a_1 = accel.linear_acceleration(a, b, c, theta_2, theta_3_1, theta_4_1, omega_2, omega_3_1, omega_4_1, alpha_2,
                                                          alpha_3_1, alpha_4_1)
        a_a_2, a_b_2, a_b_a_2 = accel.linear_acceleration(a, b, c, theta_2, theta_3_2, theta_4_2, omega_2, omega_3_2, omega_4_2, alpha_2,
                                                          alpha_3_2, alpha_4_2)

        # Position print
        print("---------------------------------------")
        print("POSITION:")
        print("Open configuration:")
        print(f"Theta_3_1 is: {theta_3_1[input_theta_2]: .2f} °")
        print(f"Theta_4_1 is: {theta_4_1[input_theta_2]: .2f} °")
        print(f"The transmission angle is: {transmission_angle_open[input_theta_2]: .2f} °\n")

        print("Crossed configuration:")
        print(f"Theta_3_2 is: {theta_3_2[input_theta_2]: .2f} °")
        print(f"Theta_4_2 is: {theta_4_2[input_theta_2]: .2f} °")
        print(f"The transmission angle is: {transmission_angle_crossed[input_theta_2]: .2f} °")
        print("---------------------------------------")

        # Velocity print
        print("VELOCITY:")
        print("Open configuration:")
        print(f"Omega_3_1 is: {omega_3_1[input_theta_2]: .2f} rad/s")
        print(f"Omega_4_1 is: {omega_4_1[input_theta_2]: .2f} rad/s")
        print(f"V_A is: {v_a: .2f} length/s")
        print(f"V_B_A_1 is: {v_b_a_1[input_theta_2]: .2f} length/s")
        print(f"V_B_1 is: {v_b_1[input_theta_2]: .2f} length/s\n")

        print("crossed configuration:")
        print(f"omega_3_2 is: {omega_3_2[input_theta_2]: .2f} rad/s")
        print(f"omega_4_2 is: {omega_4_2[input_theta_2]: .2f} rad/s")
        print(f"V_B_A_2 is: {v_b_a_2[input_theta_2]: .2f} length/s")
        print(f"V_B_2 is: {v_b_2[input_theta_2]: .2f} length/s")
        print("---------------------------------------")

        # Acceleration print
        print("ACCELERATION:")
        print("Open configuration:")
        print(f"Alpha_3_1 is: {alpha_3_1[input_theta_2]: .2f} rad/s^2")
        print(f"Alpha_4_1 is: {alpha_4_1[input_theta_2]: .2f} rad/s^2")
        print(f"A_A is: {a_a_1[input_theta_2]: .2f} length/s^2")
        print(f"A_B_A_1 is: {a_b_a_1[input_theta_2]: .2f} length/s^2")
        print(f"A_B_1 is: {a_b_1[input_theta_2]: .2f} length/s^2\n")

        print("Crossed configuration:")
        print(f"Alpha_3_2 is: {alpha_3_2[input_theta_2]: .2f} rad/s^2")
        print(f"Alpha_4_2 is: {alpha_4_2[input_theta_2]: .2f} rad/s^2")
        print(f"A_B_A_2 is: {a_b_a_2[input_theta_2]: .2f} length/s^2")
        print(f"A_B_2 is: {a_b_2[input_theta_2]: .2f} length/s^2")
        print("---------------------------------------")

        # Plots

        # Position
        # Open configiration
        plt.figure()
        plt.plot(theta_2, theta_3_1)
        plt.plot(theta_2, theta_4_1)
        plt.plot(theta_2, transmission_angle_open)
        plt.legend([r"$\theta_{3_{1}}$", r"$\theta_{4_{1}}$", r"$\mu$"])
        plt.title("Four-bar linkage position (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Angular position (°)")
        plt.grid()

        # Crossed configiration
        plt.figure()
        plt.plot(theta_2, theta_3_2)
        plt.plot(theta_2, theta_4_2)
        plt.plot(theta_2, transmission_angle_crossed)
        plt.legend([r"$\theta_{3_{2}}$", r"$\theta_{4_{2}}$", r"$\mu$"])
        plt.title("Four-bar linkage position (crossed configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Angular position (°)")
        plt.grid()
        plt.show()

        # Velocity
        # Open configuration
        plt.figure()
        plt.plot(theta_2, omega_3_1)
        plt.plot(theta_2, omega_4_1)
        plt.legend([r"$\omega_{3_{1}}$", r"$\omega_{4_{1}}$"])
        plt.title("Four-bar linkage angular velocities (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Angular velocity (rad/s)")

        plt.figure()
        plt.plot(theta_2, v_b_a_1)
        plt.plot(theta_2, v_b_1)
        plt.legend([r"$V_{{B/A}_1}$", r"$V_{B_{1}}$"])
        plt.title("Four-bar linkage linear velocities (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Linear velocity (Length/s)")

        # Crossed configuration
        plt.figure()
        plt.plot(theta_2, omega_3_2)
        plt.plot(theta_2, omega_4_2)
        plt.legend([r"$\omega_{3_{2}}$", r"$\omega_{4_{2}}$"])
        plt.title("Four-bar linkage angular velocities (crossed configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Angular velocity (rad/s)")

        plt.figure()
        plt.plot(theta_2, v_b_a_2)
        plt.plot(theta_2, v_b_2)
        plt.legend([r"$V_{{B/A}_2}$", r"$V_{B_{2}}$"])
        plt.title("Four-bar linkage linear velocities (crossed configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel("Linear velocity (Length/s)")
        plt.show()

        # Acceleration
        # Open configuration
        plt.figure()
        plt.plot(theta_2, alpha_3_1)
        plt.plot(theta_2, alpha_4_1)
        plt.legend([r"$\alpha_{3_{1}}$", r"$\alpha_{4_{1}}$"])
        plt.title("Four-bar linkage angular accelerations (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel(r"Angular accelerations (rad/$s^2$)")

        plt.figure()
        plt.plot(theta_2, a_b_a_1)
        plt.plot(theta_2, a_b_1)
        plt.legend([r"$A_{{B/A}_1}$", r"$A_{B_{1}}$"])
        plt.title("Four-bar linkage linear accelerations (open configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel(r"Linear accelerations (Length/$s^2$)")

        # Crossed configuration
        plt.figure()
        plt.plot(theta_2, alpha_3_2)
        plt.plot(theta_2, alpha_4_2)
        plt.legend([r"$\alpha_{3_{2}}$", r"$\alpha_{4_{2}}$"])
        plt.title("Four-bar linkage angular accelerations (crossed configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel(r"Angular accelerations (rad/$s^2$)")

        plt.figure()
        plt.plot(theta_2, a_b_a_2)
        plt.plot(theta_2, a_b_2)
        plt.legend([r"$A_{{B/A}_2}$", r"$A_{B_{2}}$"])
        plt.title("Four-bar linkage linear accelerations (crossed configuration)")
        plt.xlabel(r"$\theta_2\; (°)$")
        plt.ylabel(r"Linear accelerations (Length/$s^2$)")
        plt.show()

    if is_grashof is False:
        print("Therefore, no link can describe a full rotation.")
        print("Please change the lengths of your linkages so the Grashof's law is satified")


if __name__ == "__main__":
    main()
