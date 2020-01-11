
import pygame
from engine import Screen, World, Tile, Entity
from systems import System, GraphicsSystem, ControlSystem
from components import Component, Position, Camera, Control

playertile = (0,0)
playerposition = (0,0)

pygame.init()
pygame.display.set_caption('~ R I K \' S   G A M E ~')
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()

w = World(size=1024,tilesize=32)
s = Screen(800,800)

gs = GraphicsSystem()
cs = ControlSystem()

p = Entity(w)
p.camera = Camera(0,0,800,800,track=True,entitytotrack=p)
p.position = Position(0,0,32,32,2)
p.control = Control(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

running = True

while running:
    # clear screen
    s.screen.fill((0,0,0))

    # quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    System.update(w,s)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
