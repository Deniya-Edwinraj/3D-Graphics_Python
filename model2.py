import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_cylinder(radius, height, center_x, center_y, z_offset):
    z = np.linspace(0, height, 50) + z_offset
    theta = np.linspace(0, 2 * np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid) + center_x
    y_grid = radius * np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid

def create_petal(length, width, height, center_x, center_y, z_offset, angle=0):
    u = np.linspace(0, 1, 50)  
    v = np.linspace(-np.pi / 2, np.pi / 2, 50)  
    u_grid, v_grid = np.meshgrid(u, v)  

    x = length * np.sin(u_grid) * np.cos(v_grid) + center_x
    y = width * np.sin(u_grid) * np.sin(v_grid) + center_y
    z = height * u_grid ** 2 + z_offset  

    if angle != 0:
        x_rotated = x * np.cos(angle) - y * np.sin(angle)
        y_rotated = x * np.sin(angle) + y * np.cos(angle)
        return x_rotated, y_rotated, z
    return x, y, z

def create_sphere(radius, center_x, center_y, z_offset):
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = radius * np.outer(np.cos(u), np.sin(v)) + center_x
    y = radius * np.outer(np.sin(u), np.sin(v)) + center_y
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + z_offset
    return x, y, z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

stem_radius = 0.05
stem_height = 1
petal_length = 0.5
petal_width = 0.2
petal_height = 0.1
center_x, center_y = 0, 0

x_stem, y_stem, z_stem = create_cylinder(stem_radius, stem_height, center_x, center_y, 0)
ax.plot_surface(x_stem, y_stem, z_stem, color='green')

num_petals = 6
for i in range(num_petals):
    angle = i * (2 * np.pi / num_petals)  
    x_petal, y_petal, z_petal = create_petal(petal_length, petal_width, petal_height, center_x, center_y, stem_height, angle)
    ax.plot_surface(x_petal, y_petal, z_petal, color='pink')

x_bulb, y_bulb, z_bulb = create_sphere(0.1, center_x, center_y, stem_height)
ax.plot_surface(x_bulb, y_bulb, z_bulb, color='yellow')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Flower Model')

ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.5, 0.5])
ax.set_zlim([0, 1.5])

plt.show()
