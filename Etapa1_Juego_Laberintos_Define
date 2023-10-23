import numpy as np
import pygame
from pygame.locals import *

# Tamaño de la ventana
WIDTH, HEIGHT = 500, 500

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Definir título a la ventana
pygame.display.set_caption("Juego de Laberintos")

# Cargar las imágenes
pared = pygame.image.load('Images/pared1.png')
suelo = pygame.image.load('Images/ground1.png')
robot = pygame.image.load('Images/robot1.png')

# Escala de las imágenes
pared = pygame.transform.scale(pared, (50, 50))
suelo = pygame.transform.scale(suelo, (50, 50))
robot = pygame.transform.scale(robot, (50, 50))

# Cantidad de columnas y filas
columnas, filas = 10, 10

# Matriz del laberinto
mapa = np.array([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
                 [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])

"""-------------------------------------------------
Función que dibuja todos los elementos en el mapa
-------------------------------------------------"""
def map_draw():
    
    # Usar np.where para crear máscaras
    pared_mask = np.where(mapa == 1, 1, 0)
    suelo_mask = np.where(mapa == 0, 1, 0)
    
    # Tamaño de una celda en la ventana
    cell_width = WIDTH // columnas
    cell_height = HEIGHT // filas
    
    # Dibujar imágenes de "robot" y "pared" usando las máscaras
    for fil, col in np.argwhere(pared_mask == 1):
        screen.blit(pared, (col * cell_width, fil * cell_height))
    
    for fil, col in np.argwhere(suelo_mask == 1):
        screen.blit(suelo, (col * cell_width, fil * cell_height))
    
    # Dibujar al robot en la posición 0,0 del mapa
    screen.blit(robot, (0,0))

"""-------------------------------------------------
Bucle principal del programa
-------------------------------------------------"""
# Inicializa Pygame
pygame.init()  
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    # Función de dibujo
    map_draw()
    # Actualizar la ventana
    pygame.display.flip()
    
# Cerrar Pygame
pygame.quit()
