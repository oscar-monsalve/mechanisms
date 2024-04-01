# Diseñar una leva con doble detenimiento con un tipo de programa de movimiento DRDF para mover un seguidor en 0 mm durante 50°, subida de 0 mm a 55 mm durante 50°, detenimiento en 55 mm durante 50°, y bajada de 55 mm en el resto del movimiento.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Definition of beta, theta and omega
beta_1 = 50
beta_2 = beta_1 * 2
beta_3 = beta_1 * 3
beta_4 = 361 - beta_3

theta_1 = np.arange(0, beta_1+1, 1)
theta_2 = np.arange(beta_1, beta_2+1, 1)
theta_3 = np.arange(beta_2, beta_3+1, 1)
theta_4 = np.arange(beta_3, 361, 1)
theta_4_fall = np.arange(0, beta_4, 1)

omega = 2*np.pi

# Maximum height of the follower
h = 55 # milimeters

# Polinomial 3-4-5
# Define the polinomial coefficients for the polinomial 3-4-5 as "c"
c3 = 10*h
c4 = -15*h
c5 = 6*h

# Follower position by intervals
d_low_1 = [0] * (beta_1+1)
s_rise_1 = c3*(theta_1/beta_1)**3 + c4*(theta_1/beta_1)**4 + c5*(theta_1/beta_1)**5
s_fall_1 = h - ( c3*(theta_4_fall/beta_4)**3 + c4*(theta_4_fall/beta_4)**4 + c5*(theta_4_fall/beta_4)**5 )
d_high_1 = [h] * (beta_1+1) #  CHANGED THE ARGUMENT FOR [h] * [beta_1+1]

# Follower velocity

v_rise_1 = omega * 1/np.radians(beta_1) * (3*c3*(theta_1/beta_1)**2 +4*c4*(theta_1/beta_1)**3 +5*c5*(theta_1/beta_1)**4 )
v_fall_1 = -( omega * 1/np.radians(beta_4) * (3*c3*(theta_4_fall/beta_4)**2 +4*c4*(theta_4_fall/beta_4)**3 +5*c5*(theta_4_fall/beta_4)**4 ) )

# Follower acceleration
a_rise_1 = omega**2 * 1/np.radians(beta_1**2) * (6*c3*(theta_1/beta_1) + 12*c4*(theta_1/beta_1)**2 + 20*c5*(theta_1/beta_1)**3 )
a_fall_1 = -( omega**2 * 1/np.radians(beta_4**2) * (6*c3*(theta_4_fall/beta_4) + 12*c4*(theta_4_fall/beta_4)**2 + 20*c5*(theta_4_fall/beta_4)**3 ) )

# Follower jerk
j_rise_1 = omega**3 * 1/np.radians(beta_1**3) * (6*c3 + 24*c4*(theta_1/beta_1) + 60*c5*(theta_1/beta_1)**2 )
j_fall_1 = -(omega**3 * 1/np.radians(beta_4**3) * (6*c3 + 24*c4*(theta_4_fall/beta_4) + 60*c5*(theta_4_fall/beta_4)**2 ))

# Maximum values
max_v_1 = max(np.absolute(v_rise_1))
max_a_1 = max(np.absolute(a_rise_1))
max_j_1 = max(np.absolute(j_rise_1))


#______________________________________________________________________________________________________________________________________

# Define the polinomial coefficients for the polinomial 4-5-6-7 as "p"

p4 = 35*h
p5 = -84*h
p6 = 70*h
p7 = -20*h

# Follower position by intervals
d_low_2 = [0] * (beta_1+1)
s_rise_2 = p4*(theta_1/beta_1)**4 + p5*(theta_1/beta_1)**5 + p6*(theta_1/beta_1)**6 + p7*(theta_1/beta_1)**7
s_fall_2 = h - (p4*(theta_4_fall/beta_4)**4 + p5*(theta_4_fall/beta_4)**5 + p6*(theta_4_fall/beta_4)**6 + p7*(theta_4_fall/beta_4)**7)
d_high_2 = [h] * (beta_1+1) # CHANGED THE ARGUMENT FOR [h] * [beta_1+1]

# Follower velocity
v_rise_2 = omega * 1/np.radians(beta_1) * (4*p4*(theta_1/beta_1)**3 + 5*p5*(theta_1/beta_1)**4 + 6*p6*(theta_1/beta_1)**5 + 7*p7*(theta_1/beta_1)**6 )
v_fall_2 = -(omega * 1/np.radians(beta_4) * (4*p4*(theta_4_fall/beta_4)**3 + 5*p5*(theta_4_fall/beta_4)**4 + 6*p6*(theta_4_fall/beta_4)**5 + 7*p7*(theta_4_fall/beta_4)**6 ))

# Follower acceleration
a_rise_2 = omega**2 * 1/np.radians(beta_1**2) * (12*p4*(theta_1/beta_1)**2 + 20*p5*(theta_1/beta_1)**3 + 30*p6*(theta_1/beta_1)**4 + 42*p7*(theta_1/beta_1)**5 )
a_fall_2 = - ( omega**2 * 1/np.radians(beta_4**2) * (12*p4*(theta_4_fall/beta_4)**2 + 20*p5*(theta_4_fall/beta_4)**3 + 30*p6*(theta_4_fall/beta_4)**4 + 42*p7*(theta_4_fall/beta_4)**5 ) )

# Follower jerk
j_rise_2 = omega**3 * 1/np.radians(beta_1**3) * (24*p4*(theta_1/beta_1) + 60*p5*(theta_1/beta_1)**2 + 120*p6*(theta_1/beta_1)**3 + 210*p7*(theta_1/beta_1)**4 )
j_fall_2 = -(omega**3 * 1/np.radians(beta_4**3) * (24*p4*(theta_4_fall/beta_4) + 60*p5*(theta_4_fall/beta_4)**2 + 120*p6*(theta_4_fall/beta_4)**3 + 210*p7*(theta_4_fall/beta_4)**4 ))

# Maximum values
max_v_2 = max(np.absolute(v_rise_2))
max_a_2 = max(np.absolute(a_rise_2))
max_j_2 = max(np.absolute(j_rise_2))

# Print maximum values for the polinomial 3-4-5
print("The maximum values for the polinomial 3-4-5 are:")
print("The maximum velocity is: ", format(max_v_1, ".2f"), " mm/s")
print("The maximum acceleration is: ", format(max_a_1, ".2f"), " mm/s^2")
print("The maximum jerk is: ", format(max_j_1, ".2f"), " mm/s^3")
print()


# Print maximum values for the polinomial 4-5-6-7
print("The maximum values for the polinomial 4-5-6-7 are:")
print("The maximum velocity is: ", format(max_v_2, ".2f"), " mm/s")
print("The maximum acceleration is: ", format(max_a_2, ".2f"), " mm/s^2")
print("The maximum jerk is: ", format(max_j_2, ".2f"), " mm/s^3")

# ______________________________________________________________________________________________________________________________________
# Export the polinomials as a .txt file

# normalized polinomial 3-4-5


# x_1 = theta_1/beta_1
# y_1 = s_rise_1/h

# data_1 = np.column_stack((x_1, y_1))

# np.savetxt("grupo_9_polinomio_3-4-5.txt", data_1, delimiter = ";", fmt = "%.4f")

# # Normalized polinomial 4-5-6-7

# x_2 = theta_1/beta_1
# y_2 = s_rise_2/h

# data_2 = np.column_stack((x_2, y_2))

# np.savetxt("grupo_9_polinomio_4-5-6-7.txt", data_2, delimiter = ";", fmt = "%.4f")

# ______________________________________________________________________


# Import cam images 

image_path = "D:/OneDrive - Instituto Tecnológico Metropolitano/ITM/2. Teaching/2. Catedra/1. Mecanismos/Evaluación/6. Diseño_levas (20%)/Soluciones_ejercicios_levas/CAD_levas/Grupo_2.PNG"


# LAB
# image_path = "C:/Users/cadd.ITMROBLEDO/OneDrive - Instituto Tecnológico Metropolitano/ITM/2. Teaching/2. Catedra/1. Mecanismos/Evaluación/6. Diseño_levas (20%)/Soluciones_ejercicios_levas/CAD_levas/Grupo_2.PNG" 

# LAPTOP
# image_path = "C:/Users/Oscar Monsalve/OneDrive - INSTITUTO TECNOLOGICO METROPOLITANO - ITM/ITM/2. Teaching/2. Catedra/1. Mecanismos/Evaluación/6. Diseño_levas (20%)/Soluciones_ejercicios_levas/CAD_levas/Grupo_2.PNG"

image = mpimg.imread(image_path)

# ________________________________________________________________________
# Plots for the polinomial 3-4-5

fig, p1 = plt.subplots(4, 1, sharex= True)

p1[0].plot(
    theta_1, d_low_1,
    theta_2, s_rise_1,
    theta_3, d_high_1,
    theta_4, s_fall_1,
    label = "Desplazamiento"
)

p1[1].plot(
    theta_1, d_low_1,
    theta_2, v_rise_1,
    theta_3, d_low_1,
    theta_4, v_fall_1,
    label = "Velocidad"
)

p1[2].plot(
    theta_1, d_low_1,
    theta_2, a_rise_1,
    theta_3, d_low_1,
    theta_4, a_fall_1,
    label = "Aceleración"
)

p1[3].plot(
    theta_1, d_low_1,
    theta_2, j_rise_1,
    theta_3, d_low_1,
    theta_4, j_fall_1,
    label = "Sobreaceleración"
)

# x-axis parameters
plt.xlabel(r"$\theta$ (°)")
plt.xlim([0,360])
plt.xticks([0, beta_1, beta_2, beta_3, 360])


# Plots for the polinomial 4-5-6-7

fig, p2 = plt.subplots(4, 1, sharex= True)

p2[0].plot(
    theta_1, d_low_2,
    theta_2, s_rise_2,
    theta_3, d_high_2,
    theta_4, s_fall_2,
    label = "Desplazamiento"
)

p2[1].plot(
    theta_1, d_low_2,
    theta_2, v_rise_2,
    theta_3, d_low_2,
    theta_4, v_fall_2,
    label = "Velocidad"
)

p2[2].plot(
    theta_1, d_low_2,
    theta_2, a_rise_2,
    theta_3, d_low_2,
    theta_4, a_fall_2,
    label = "Aceleración"
)

p2[3].plot(
    theta_1, d_low_2,
    theta_2, j_rise_2,
    theta_3, d_low_2,
    theta_4, j_fall_2,
    label = "Sobreaceleración"
)

# x-axis parameters
plt.xlabel(r"$\theta$ (°)")
plt.xlim([0,360])
plt.xticks([0, beta_1, beta_2, beta_3, 360])


# Titles for both plots
p1[0].set_title("Diagrama S V A J: polinomio 3-4-5")
p2[0].set_title("Diagrama S V A J: polinomio 4-5-6-7")

# y-axis titles for both plots
p1[0].set_ylabel("s (mm)", fontsize=12)
p1[1].set_ylabel("v (mm/s)", fontsize=12)
p1[2].set_ylabel("a $(mm/s^2)$", fontsize=12)
p1[3].set_ylabel("j $(mm/s^3)$", fontsize=12)

p2[0].set_ylabel("s (mm)", fontsize=12)
p2[1].set_ylabel("v (mm/s)", fontsize=12)
p2[2].set_ylabel("a $(mm/s^2)$", fontsize=12)
p2[3].set_ylabel("j $(mm/s^3)$", fontsize=12)


# Plot the imported image of the cam
plt.figure()
plt.imshow(image)

# Title
plt.title("Modelo CAD de la leva", fontsize=14)
plt.xticks([])
plt.yticks([])


plt.tight_layout()
plt.show()

