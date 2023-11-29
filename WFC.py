import numpy as np
import matplotlib.pyplot as plt

# Definir las figuras
figure1 = np.array([[0, 1, 1, 0],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [0, 1, 1, 0]])

figure2 = np.array([[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]])

figure3 = np.array([[1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0]])

figure4 = np.array([[0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1]])

# Concatenar las figuras en una lista
figure_list = np.array([figure1, figure2, figure3, figure4])

# Definir la función para elegir una figura aleatoria
def choose_figure(figure_list):
    # Seleccionar una figura aleatoria de la lista
    figure_choice = figure_list[np.random.choice(len(figure_list))]
    return figure_choice

# Definir el tamaño del tablero de juego
board_size = (64, 64)

# Crear la matriz de juego inicial
game_board = np.zeros(board_size)

# Definir el tamaño de las figuras
figure_size = (4, 4)

# Llenar la matriz de juego con figuras aleatorias
for i in range(0, board_size[0], figure_size[0]):
    for j in range(0, board_size[1], figure_size[1]):
        figure = choose_figure(figure_list)
        game_board[i:i+figure_size[0], j:j+figure_size[1]] = figure


# Mostrar la matriz de juego
plt.imshow(game_board, cmap='gray')
plt.show()
