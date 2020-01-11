class Component():
    def __init__(self):
        pass

class Camera(Component):
    def __init__(self,x,y,w,h,track=True,entitytotrack=None):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bg = (100,100,100)
        if track:
            self.track = True
        else:
            self.track = False
        self.entitytotrack = entitytotrack
        self.worldx = 0
        self.worldy = 0

class Position(Component):
    def __init__(self,x,y,w,h,s):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = s

class Control(Component):
    def __init__(self,u,d,l,r):
        super().__init__()
        self.up = u
        self.down = d
        self.left = l
        self.right = r
