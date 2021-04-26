import noise
import random

from modules.constants import *
from modules.colors import *

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
                y = noise.pnoise2(xLoop * .02 + xOffset, zLoop * .02 + zOffset, octaves = NOISE_OCTAVES)
                color = SEA_COLOR

                if y > -0.1:
                    color = SHORE_COLOR
                if y > 0.05:
                    color = SAND_COLOR
                if y > 0.1:
                    color = GRASS_COLOR
                if y > 0.2:
                    color = HILL_COLOR
                if y > 0.3:
                    color = MOUNTAIN_COLOR
                if y > 0.4:
                    color = SNOW_COLOR

                tileObject = Tile(xLoop, y, zLoop, color)
                self.tiles.append(tileObject)
