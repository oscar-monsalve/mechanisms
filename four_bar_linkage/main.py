# import matplotlib.pyplot as plt
import position as pos
import grashof as grashof
import velocity as vel

# four-bar linkage data
a = 40
b = 120
c = 80
d = 100
theta_2 = 40  # degrees
omega_2 = 25  # rad/s


def main() -> None:
    is_grashof = grashof.is_grashof(a, b, c, d)

    if is_grashof is True:
        # Position
        k1, k2, k3, k4, k5 = pos.k_constants(a, b, c, d)
        A, B, C, D, F, E = pos.A_constants(theta_2, k1, k2, k3, k4, k5)
        theta_3_1, theta_4_1, transmission_angle_open = pos.position_open(A, B, C, D, F, E)
        theta_3_2, theta_4_2, transmission_angle_crossed = pos.position_crossed(A, B, C, D, F, E)

        # Velocity
        omega_3_1, omega_4_1 = vel.angular_velocities(a, b, c, theta_2, theta_3_1, theta_4_1, omega_2)
        omega_3_2, omega_4_2 = vel.angular_velocities(a, b, c, theta_2, theta_3_2, theta_4_2, omega_2)
        v_a, v_b_a, v_b = vel.linear_velocities(a, b, c, omega_2, omega_3_1, omega_4_1)

        # Position print
        print("---------------------------------------")
        print("Position:")
        print("Open configuration:")
        print(f"Theta_3_1 is: {theta_3_1: .2f} °")
        print(f"Theta_4_1 is: {theta_4_1: .2f} °")
        print(f"The transmission angle is: {transmission_angle_open: .2f} °\n")

        print("Crossed configuration:")
        print(f"Theta_3_2 is: {theta_3_2: .2f} °")
        print(f"Theta_4_2 is: {theta_4_2: .2f} °")
        print(f"The transmission angle is: {transmission_angle_crossed: .2f} °")
        print("---------------------------------------\n")

        # Velocity print
        print("Velocity:")
        print("Open configuration:")
        print(f"Omega_3_1 is: {omega_3_1: .2f} rad/s")
        print(f"Omega_3_1: {omega_4_1: .2f} rad/s")
        print(f"V_A is: {v_a: .2f} length/s")
        print(f"V_B_A is: {v_b_a: .2f} length/s")
        print(f"V_B is: {v_b: .2f} length/s\n")

        print("Crossed configuration:")
        print(f"Omega_3_2 is: {omega_3_2: .2f} rad/s")
        print(f"Omega_3_1 is: {omega_4_2: .2f} rad/s")
        print("---------------------------------------\n")

    if is_grashof is False:
        print("Therefore, no link can describe a full rotation.")
        print("Please change the lengths of your linkages so the Grashof's law is satified")


if __name__ == "__main__":
    main()
