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
                moving = False
                if keys[e.control.left]:
                    e.position.x -= e.position.speed
                    moving = True
                    e.state.state = 'left'
                if keys[e.control.right]:
                    e.position.x += e.position.speed
                    moving = True
                    e.state.state = 'right'
                if keys[e.control.up]:
                    e.position.y -= e.position.speed
                    moving = True
                    e.state.state = 'up'
                if keys[e.control.down]:
                    e.position.y += e.position.speed
                    moving = True
                    e.state.state = 'down'
                
                if not moving:
                    e.state.state = 'idle'

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
                tw = int(c.w / world.tilesize)
                th = int(c.h / world.tilesize)

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
                    screen.screen.blit(o.sprite.sprites[o.state.state][o.sprite.index], (xpos,ypos))

                screen.screen.set_clip()

class SpriteSystem(System):
    def __init__(self):
        super().__init__()
    def update(self, world, screen):
        for e in world.entities:
            if e.sprite != None and e.state != None:
                if e.sprite.animate:
                    e.sprite.animationTimer += 1
                    if e.sprite.animationTimer > e.sprite.animationSpeed:
                        e.sprite.animationTimer = 0
                        e.sprite.index += 1
                        if e.sprite.index > (len(e.sprite.sprites[e.state.state]) - 1):
                            e.sprite.index = 0