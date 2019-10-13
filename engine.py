import noise
import numpy as np
import pygame
import random

blue = (0,0,255)
green = (0,255,0)
darkgreen = (0,155,0)
yellow = (255,255,0)

grass = pygame.image.load('grass.png')
forest = pygame.image.load('forest.png')
beach = pygame.image.load('beach.png')
sea = pygame.image.load('sea.png')

class Screen():
    def __init__(self,w,h):
        self.screen = pygame.display.set_mode((w,h))
        self.w = w
        self.h = h

class Tile():
    def __init__(self,image):
        self.image = image

class World():
    def __init__(self,size,tilesize):
        self.entities = []
        self.tilesize = tilesize
        self.size = size
        scale = 150.0
        octaves = 4
        persistence = 0.5
        lacunarity = 2.0
        seed = int(random.random()*100)

        noisemap = np.zeros((size,size))
        self.tilemap = [[None for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                noisemap[i][j] = noise.pnoise2(i/scale,
                                            j/scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=size,
                                            repeaty=size,
                                            base=0)#seed)

        # replace numbers with tiles
        for i in range(size):
            for j in range(size):
                if noisemap[i][j] < 0.1:
                    img = grass
                elif noisemap[i][j] < 0.2:
                    img = forest
                elif noisemap[i][j] < 0.25:
                    img = beach
                elif noisemap[i][j] < 0.27:
                    img = sea
                else:
                    img = grass
                self.tilemap[i][j] = Tile(img)

class Entity():
    def __init__(self, world, camera=None, position=None, control=None):
        self.position = position
        self.camera   = camera
        self.control  = control
        world.entities.append(self)
