# import matplotlib.pyplot as plt
import position as pos

# four-bar linkage data
theta_2 = 40  # degrees
a = 40
b = 120
c = 80
d = 100


def main() -> None:
    k1, k2, k3, k4, k5 = pos.k_constants(a, b, c, d)
    A, B, C, D, F, E = pos.A_constants(theta_2, k1, k2, k3, k4, k5)
    theta_3_1, theta_4_1, transmission_angle_open = pos.position_open(A, B, C, D, F, E)
    theta_3_2, theta_4_2, transmission_angle_crossed = pos.position_crossed(A, B, C, D, F, E)

    print("Open configuration:")
    print(f"Theta_3_1 is: {theta_3_1: .2f} °")
    print(f"Theta_4_1 is: {theta_4_1: .2f} °\n")
    print(f"The transmission angle is: {transmission_angle_open: .2f}")

    print("Crossed configuration:")
    print(f"Theta_3_2 is: {theta_3_2: .2f} °")
    print(f"Theta_4_2 is: {theta_4_2: .2f} °\n")
    print(f"The transmission angle is: {transmission_angle_crossed: .2f}")


if __name__ == "__main__":
    main()
