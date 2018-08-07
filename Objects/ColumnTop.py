from GameFrame import RoomObject, Globals


class ColumnTop(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image('column.png')
        self.set_image(image, 80, 550)

    def step(self):
        self.x -= Globals.scroll_speed
        if self.x < -80:
            self.delete_object(self)
