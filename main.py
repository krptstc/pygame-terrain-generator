import pygame
pygame.init()

from modules.constants import *
from modules.world import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terrain Generator')

world = World()
world.generate(SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                world.generate(SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE)

    SCREEN.fill((0, 0, 0))

    for tile in world.tiles:
        pygame.draw.rect(SCREEN, tile.color, pygame.Rect(tile.x * TILE_SIZE, tile.z * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()
