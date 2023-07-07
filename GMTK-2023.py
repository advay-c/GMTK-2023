import pygame
import random
import os

pygame.font.init()

WIDTH, HEIGHT = 750, 750
GROUND = pygame.image.load(os.path.join('gmtk-assets', 'ground.png'))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GMTK-2023")

run = True
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    WINDOW.blit(GROUND, (0, 0)) #placing image on screen
    pygame.display.update()


pygame.quit()