import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices = np.array([
    [14, 7, 5],
    [11, 12, 5],
    [5, 12, 5],
    [2, 7, 5],
    [5, 2, 5],
    [11, 2, 5],
    [14, 7, 15],
    [11, 12, 15],
    [5, 12, 15],
    [2, 7, 15],
    [5, 2, 15],
    [11, 2, 15],
])

faces = np.array([
    [0, 1, 7, 6],
    [1, 2, 8, 7],
    [2, 3, 9, 8],
    [3, 4, 10, 9],
    [4, 5, 11, 10],
    [5, 0, 6, 11]
])

basement = np.array([
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10, 11]
])

prism = [Poly3DCollection([vertices[face] for face in faces], alpha=1, facecolor='grey', edgecolor='k')]
base = [Poly3DCollection([vertices[x] for x in basement], alpha=1, facecolor='grey', edgecolor='k')]
ax.add_collection3d(base[0])
ax.add_collection3d(prism[0])
ax.auto_scale_xyz([0, 20], [0, 20], [0, 20])
plt.show()
