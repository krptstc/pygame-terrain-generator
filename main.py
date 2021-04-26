import pygame
import noise
pygame.init()

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480
TILE_SIZE     = 16

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Terrain Generator')

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
        for xLoop in range(x):
            for zLoop in range(z):
                y = noise.pnoise2(xLoop * .05, zLoop * .05)
                color = (0, 255, 0)

                if y > 0:
                    color = (255, 0, 0)

                tileObject = Tile(xLoop, y, zLoop, color)
                self.tiles.append(tileObject)

world = World()
world.generate(SCREEN_WIDTH // TILE_SIZE, SCREEN_HEIGHT // TILE_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for tile in world.tiles:
        print("Tile")
        print(f"X: {tile.x}")
        print(f"Y: {tile.y}")
        print(f"Z: {tile.z}")
        print(f"Color: {tile.color}")

    pygame.display.update()
