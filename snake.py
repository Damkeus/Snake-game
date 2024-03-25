import pygame
import random

pygame.init()

#les couleurs
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

# Taille de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Taille de la grille
grid_size = 20
grid_width = screen_width // 2 * grid_size
grid_height = screen_height // 2 * grid_size

# Vitesse du serpent
snake_speed = 8

# Position intiale du serpent
snake_x = grid_width // 2 * grid_size
snake_y = grid_height // 2  * grid_size 

# Direction initale du serpent
snake_direction = "RIGHT"  

# Taille de départ
snake_lenght = 1
snake_body = [(snake_x,snake_y)]

# Définition de la position initial du fruit
fruit_x = random.randint(0,grid_width - 1) * grid_size
fruit_y = random.randint(0, grid_height - 1) * grid_size
