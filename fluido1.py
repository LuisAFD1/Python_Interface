import pygame
import numpy as np

# Configuración de la simulación
width, height = 800, 600
grid_size = 5
viscosity = 0.1
dt = 0.1

# Inicialización de la ventana de Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Fluidos")

# Creación de la cuadrícula de velocidades
u = np.zeros((width // grid_size, height // grid_size))
v = np.zeros((width // grid_size, height // grid_size))

def draw_fluid():
    for i in range(u.shape[0]):
        for j in range(u.shape[1]):
            x = i * grid_size
            y = j * grid_size
            pygame.draw.line(screen, (255, 255, 255), (x, y), (x + u[i, j], y + v[i, j]), 2)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualización de la simulación
    # Aquí es donde implementarías las ecuaciones de fluidos
    # En este ejemplo, solo agrego un poco de movimiento vertical
    v[1, :] += 0.1

    # Difusión
    u[1:-1, 1:-1] += viscosity * (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4 * u[1:-1, 1:-1])
    v[1:-1, 1:-1] += viscosity * (v[2:, 1:-1] + v[:-2, 1:-1] + v[1:-1, 2:] + v[1:-1, :-2] - 4 * v[1:-1, 1:-1])

    # Advección
    u[1:-1, 1:-1] -= dt * u[1:-1, 1:-1] * (u[2:, 1:-1] - u[:-2, 1:-1] + u[1:-1, 2:] - u[1:-1, :-2]) / (2 * grid_size)
    v[1:-1, 1:-1] -= dt * v[1:-1, 1:-1] * (v[2:, 1:-1] - v[:-2, 1:-1] + v[1:-1, 2:] - v[1:-1, :-2]) / (2 * grid_size)

    # Dibujar la simulación en la ventana de Pygame
    screen.fill((0, 0, 0))
    draw_fluid()
    pygame.display.flip()

pygame.quit()
