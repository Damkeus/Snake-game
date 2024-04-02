import pygame
import random

# initalise le jeu
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Taille de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Taille de la grille
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Vitesse du serpent
snake_speed = 10

# Position inital du serpent
snake_x = grid_width // 2 * grid_size
snake_y = grid_height // 2 * grid_size

# Direction inital du serpent
snake_direction = "RIGHT"

# Taille de départ
snake_length = 10
snake_body = [(snake_x, snake_y)]

# Position initial du fruit
fruit_x = random.randint(0, grid_width - 1) * grid_size
fruit_y = random.randint(0, grid_height - 1) * grid_size

# Game loop control
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Movement controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Actualise la position du serpent
    if snake_direction == "UP":
        snake_y -= grid_size
    elif snake_direction == "DOWN":
        snake_y += grid_size
    elif snake_direction == "LEFT":
        snake_x -= grid_size
    elif snake_direction == "RIGHT":
        snake_x += grid_size

    # Condition de game over
    if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
        running = False  # End game if snake hits the boundaries

    # Méchanique du corp du serpent
    snake_body.insert(0, (snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[-1]

    # Vérifie les colision du serpent
    for block in snake_body[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            running = False  # Met fin aub jeu si colision

    # Colision du fruit
    if snake_x == fruit_x and snake_y == fruit_y:
        fruit_x = random.randint(0, grid_width - 1) * grid_size
        fruit_y = random.randint(0, grid_height - 1) * grid_size
        snake_length += 1

    # Dessin 
    screen.fill(BLACK)
    for part in snake_body:
        pygame.draw.rect(screen, GREEN, [part[0], part[1], grid_size, grid_size])

    pygame.draw.rect(screen, RED, [fruit_x, fruit_y, grid_size, grid_size])

    pygame.display.update()

    # Control du taux de rafraichissement
    clock.tick(snake_speed)

pygame.quit()
