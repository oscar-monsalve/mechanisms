# import matplotlib.pyplot as plt
import position as pos
import grashof as grashof

# four-bar linkage data
theta_2 = 30  # degrees
a = 38
b = 56
c = 50
d = 66


def main() -> None:
    is_grashof = grashof.is_grashof(a, b, c, d)

    if is_grashof is True:

        k1, k2, k3, k4, k5 = pos.k_constants(a, b, c, d)
        A, B, C, D, F, E = pos.A_constants(theta_2, k1, k2, k3, k4, k5)
        theta_3_1, theta_4_1, transmission_angle_open = pos.position_open(A, B, C, D, F, E)
        theta_3_2, theta_4_2, transmission_angle_crossed = pos.position_crossed(A, B, C, D, F, E)

        print("Open configuration:")
        print(f"Theta_3_1 is: {theta_3_1: .2f} °")
        print(f"Theta_4_1 is: {theta_4_1: .2f} °")
        print(f"The transmission angle is: {transmission_angle_open: .2f} °\n")

        print("Crossed configuration:")
        print(f"Theta_3_2 is: {theta_3_2: .2f} °")
        print(f"Theta_4_2 is: {theta_4_2: .2f} °")
        print(f"The transmission angle is: {transmission_angle_crossed: .2f} °\n")

    if is_grashof is False:
        print("Therefore, no link can describe a full rotation.")
        print("Please change the lengths of your linkages so the Grashof's law is satified")


if __name__ == "__main__":
    main()
