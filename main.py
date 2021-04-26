import pygame
import noise
import random
pygame.init()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
TILE_SIZE     = 2

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terrain Generator')

SEA_COLOR     = (0, 0, 160)
SHORE_COLOR   = (0, 0, 200)
SAND_COLOR    = (200, 200, 0)
GRASS_COLOR   = (0, 200, 0)
HILL_COLOR    = (0, 160, 0)
NOISE_OCTAVES = 4

class Tile:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

class World:
    def __init__(self):
        self.tiles = []

    def generate(self, x, z):
        xOffset = random.randint(-4096, 4096)
        zOffset = random.randint(-4096, 4096)
        self.tiles = []
        for xLoop in range(x):
            for zLoop in range(z):
                y = noise.pnoise2(xLoop * .02 + xOffset, zLoop * .02 + zOffset, octaves=NOISE_OCTAVES)
                color = SEA_COLOR

                if y > -0.1:
                    color = SHORE_COLOR
                if y > 0.05:
                    color = SAND_COLOR
                if y > 0.1:
                    color = GRASS_COLOR
                if y > 0.2:
                    color = HILL_COLOR

                tileObject = Tile(xLoop, y, zLoop, color)
                self.tiles.append(tileObject)

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
