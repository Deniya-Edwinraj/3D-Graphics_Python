import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_cylinder(radius, height, center_x, center_y, z_offset):
    z = np.linspace(0, height, 50) + z_offset
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid) + center_x
    y_grid = radius * np.sin(theta_grid) + center_y
    return x_grid, y_grid, z_grid

def create_cone(radius, height, center_x, center_y, z_offset):
    z = np.linspace(0, height, 50) + z_offset
    theta = np.linspace(0, 2*np.pi, 50)
    r = np.linspace(radius, 0, 50)  
    r_grid, theta_grid = np.meshgrid(r, theta)
    x_grid = r_grid * np.cos(theta_grid) + center_x
    y_grid = r_grid * np.sin(theta_grid) + center_y
    z_grid = np.outer(np.ones(50), z)
    return x_grid, y_grid, z_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

trunk_radius = 0.1
trunk_height = 1
cone_radius = 0.5
cone_height = 1
center_x, center_y = 0, 0

x_trunk, y_trunk, z_trunk = create_cylinder(trunk_radius, trunk_height, center_x, center_y, 0)
ax.plot_surface(x_trunk, y_trunk, z_trunk, color='brown')

x_cone, y_cone, z_cone = create_cone(cone_radius, cone_height, center_x, center_y, trunk_height)
ax.plot_surface(x_cone, y_cone, z_cone, color='green')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Tree Model')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 2])

plt.show()
