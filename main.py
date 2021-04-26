import pygame
import noise
pygame.init()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
TILE_SIZE     = 16

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terrain Generator')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
