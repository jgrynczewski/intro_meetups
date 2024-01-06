# Gra II - fajerwerki (na dowolny klawisz)

import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fajerwerki")

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)

# Klasa reprezentująca pojedynczą cząstkę fajerwerku
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = random.randint(2, 5)
        self.vel = random.randint(1, 5)

    def move(self):
        self.y -= self.vel

# Lista przechowująca cząstki fajerwerku
particles = []

# Pętla gry
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Dodaj nową cząstkę fajerwerku po naciśnięciu klawisza
            particles.append(Particle(random.randint(0, width), height))

    # Ruch cząstek fajerwerku
    for particle in particles:
        particle.move()

    # Usuwanie cząstek, które przekroczyły górny kraniec ekranu
    particles = [particle for particle in particles if particle.y > 0]

    # Rysowanie obiektów
    win.fill(black)
    for particle in particles:
        pygame.draw.circle(win, particle.color, (particle.x, int(particle.y)), particle.size)

    pygame.display.flip()
    clock.tick(60)
