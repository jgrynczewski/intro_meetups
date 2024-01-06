# Gra - ping-pong

import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gra w Pong")

# Paletki
player1 = pygame.Rect(50, height // 2 - 50, 20, 100)
player2 = pygame.Rect(width - 70, height // 2 - 50, 20, 100)

# Piłka
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
ball_speed = [5, 5]

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)

# Pętla gry
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < height:
        player1.y += 5
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < height:
        player2.y += 5

    # Ruch piłki
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Odbicie piłki od ścian
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]

    # Kolizje z paletkami
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    # Wygrana
    if ball.left <= 0 or ball.right >= width:
        ball.x = width // 2 - 15
        ball.y = height // 2 - 15
        ball_speed[0] = -ball_speed[0]

    # Rysowanie obiektów
    win.fill(black)
    pygame.draw.rect(win, white, player1)
    pygame.draw.rect(win, white, player2)
    pygame.draw.ellipse(win, white, ball)

    pygame.display.flip()
    clock.tick(60)
