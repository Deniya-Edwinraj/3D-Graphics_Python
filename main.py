import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

base_vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                          [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])  

faces = [[base_vertices[j] for j in [0, 1, 2, 3]],  
         [base_vertices[j] for j in [4, 5, 6, 7]], 
         [base_vertices[j] for j in [0, 1, 5, 4]], 
         [base_vertices[j] for j in [2, 3, 7, 6]],
         [base_vertices[j] for j in [1, 2, 6, 5]],
         [base_vertices[j] for j in [4, 7, 3, 0]]]

ax.add_collection3d(Poly3DCollection(faces, facecolors='lightblue', linewidths=1, edgecolors='r', alpha=.25))

roof_vertices = np.array([[0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0.5, 0.5, 1.5]])

roof_faces = [[roof_vertices[j] for j in [0, 1, 4]], 
              [roof_vertices[j] for j in [1, 2, 4]],
              [roof_vertices[j] for j in [2, 3, 4]],
              [roof_vertices[j] for j in [3, 0, 4]]]

ax.add_collection3d(Poly3DCollection(roof_faces, facecolors='brown', linewidths=1, edgecolors='r', alpha=.5))

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D House Model')

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1.5])

plt.show()
