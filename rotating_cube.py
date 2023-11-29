import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from matplotlib.animation import FuncAnimation


# Definir las coordenadas de los vértices del cubo
vertices = np.array([[-0.5, -0.5, -0.5],
                     [0.5, -0.5, -0.5],
                     [0.5, 0.5, -0.5],
                     [-0.5, 0.5, -0.5],
                     [-0.5, -0.5, 0.5],
                     [0.5, -0.5, 0.5],
                     [0.5, 0.5, 0.5],
                     [-0.5, 0.5, 0.5]])

# Definir las caras del cubo
caras = np.array([[0, 1, 2, 3],
                  [1, 5, 6, 2],
                  [5, 4, 7, 6],
                  [4, 0, 3, 7],
                  [0, 4, 5, 1],
                  [3, 2, 6, 7]])

# Función que anima el cubo
def animar(i):
    ax.clear()
    theta = i * np.pi / 50
    rotacion = np.array([[np.cos(theta), -np.sin(theta), 0],
                         [np.sin(theta), np.cos(theta), 0],
                         [0, 0, 1]])
    vertices_rotados = vertices.dot(rotacion)
    ax.add_collection3d(
        Poly3DCollection([vertices_rotados[caras[i]] for i in range(6)],
                         facecolors='b', edgecolors='k', linewidths=1, alpha=0.5))
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    return ax

# Crear la figura 3D y animar el cubo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
animacion = FuncAnimation(fig, animar, frames=100, interval=100)
plt.show()
