"""------------------------------------------------
Created on Wed Oct 25 13:58:37 2023
@author: Santiago Lasso
------------------------------------------------"""
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
robot_left = pygame.image.load('Images/robot1_left.png')

out1 = pygame.image.load('Images/out1.png') 
fin_bg = pygame.image.load('Images/bg_winner.png') 

# Escala de las imágenes
pared = pygame.transform.scale(pared, (50, 50))
suelo = pygame.transform.scale(suelo, (50, 50))
robot = pygame.transform.scale(robot, (50, 50))
robot_left = pygame.transform.scale(robot_left, (50, 50))

out1 = pygame.transform.scale(out1, (50, 50))
fin_bg = pygame.transform.scale(fin_bg, (WIDTH, HEIGHT))

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

# Posición inicial del robot
pos_x, pos_y = 0, 0

# Dirección inicial del robot
direccion = 'derecha'

# Posición de salida del laberinto
salida_x, salida_y = 9, 9

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
    
    # Dibuja al robot en función de su dirección
    if direccion == 'derecha' or direccion == 'arriba' or direccion == 'abajo':
        screen.blit(robot, (pos_x * cell_width, pos_y * cell_height))
        
    elif direccion == 'izquierda':
        screen.blit(robot_left, (pos_x * cell_width, pos_y * cell_height))
    
    # Dibujar la salida en la posición 9,9 del mapa
    screen.blit(out1, (9 * cell_width,9* cell_height))
    
    if fin:
        # Cuando el robot llega a la salida, dibuja la imagen de fondo "fin_bg"
        screen.blit(fin_bg, (0, 0))

"""-------------------------------------------------
Bucle principal del programa
-------------------------------------------------"""
# Inicializa Pygame
pygame.init()  
    
running = True
fin = False

while running:
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        
        # Verifica las teclas presionadas para mover el robot
        elif event.type == KEYDOWN:
            
            if not fin:  # Solo permite el movimiento si el robot ha llegado a la "salida"
            
                # Si se presiona la flecha de arriba (↑)
                if event.key == K_UP and (pos_y > 0) and mapa[pos_y-1, pos_x] == 0:
                    pos_y -= 1
                    direccion = 'arriba'
                    
                # Si se presiona la flecha de abajo (↓)
                elif event.key == K_DOWN and (pos_y < filas-1) and mapa[pos_y+1, pos_x] == 0:
                    pos_y += 1
                    direccion = 'abajo'
                    
                # Si se presiona la flecha derecha (→)
                elif event.key == K_RIGHT and (pos_x < columnas - 1) and mapa[pos_y, pos_x + 1] == 0:
                    pos_x += 1
                    direccion = 'derecha'
                    
                # Si se presiona la flecha izquierda (←)
                elif event.key == K_LEFT and (pos_x > 0) and mapa[pos_y, pos_x - 1] == 0:
                    pos_x -= 1
                    direccion = 'izquierda'
    
    # Verifica si el robot ha llegado a la posición de salida
    if not fin and pos_x == salida_x and pos_y == salida_y:
        fin = True
        
    # Función de dibujo
    map_draw()

    # Actualizar la ventana
    pygame.display.flip()
    
# Cerrar Pygame
pygame.quit()
