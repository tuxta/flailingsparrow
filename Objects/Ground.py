from GameFrame import RoomObject, Globals


class Ground(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image('ground.png')
        self.set_image(image, 800, 101)

    def step(self):
        self.x -= Globals.scroll_speed
        if self.x <= -800:
            self.x = 800
