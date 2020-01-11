import pygame

class System():
    systems = []
    @classmethod
    def update(cls, world, screen):
        for s in cls.systems:
            s.update(world, screen)
    def __init__(self):
        self.systems.append(self)

class ControlSystem(System):
    def __init__(self):
        super().__init__()
    def update(self, world, screen):
        for e in world.entities:
            if e.control != None:
                keys=pygame.key.get_pressed()
                if keys[e.control.left]:
                    e.position.x -= e.position.speed
                if keys[e.control.right]:
                    e.position.x += e.position.speed
                if keys[e.control.up]:
                    e.position.y -= e.position.speed
                if keys[e.control.down]:
                    e.position.y += e.position.speed

class GraphicsSystem(System):
    def __init__(self):
        super().__init__()
    def update(self, world, screen):
        for e in world.entities:

            if e.camera:

                c = e.camera
                screen.screen.set_clip(pygame.Rect(c.x,c.y,c.w,c.h))
                screen.screen.fill(c.bg)

                # track
                if c.track and c.entitytotrack != None:
                    c.worldx = c.entitytotrack.position.x + (c.entitytotrack.position.w/2)
                    c.worldy = c.entitytotrack.position.y + (c.entitytotrack.position.h/2)

                # calculate entity tile position
                tilex = int(e.position.x / world.tilesize)
                tiley = int(e.position.y / world.tilesize)
                # calculate number of tiles that can be displayed
                tw = int(c.w / world.tilesize)# / 2) + int(100/world.tilesize)
                th = int(c.h / world.tilesize)# / 2) + int(100/world.tilesize)

                # draw world
                for i in range(max(0,tilex - tw), min(world.size,tilex + tw)):
                    for j in range(max(0,tiley - th), min(world.size,tiley + th)):
                        img = world.tilemap[i][j].image
                        xp = c.x + (c.w/2) - c.worldx + (i * world.tilesize)
                        yp = c.y + (c.h/2) - c.worldy + (j * world.tilesize)
                        screen.screen.blit(img,(xp,yp))

                # draw all entities
                for o in world.entities:
                    xpos = c.x + (c.w/2) - c.worldx + o.position.x
                    ypos = c.y + (c.h/2) - c.worldy + o.position.y
                    pygame.draw.rect(screen.screen,(0,0,255),pygame.Rect(xpos,ypos,o.position.w,o.position.h))

                screen.screen.set_clip()
