from GameFrame import RoomObject, Globals


class ColumnBottom(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image('column.png')
        self.set_image(image, 80, 550)
        self.scored = False

    def step(self):
        self.x -= Globals.scroll_speed
        if self.x + 70 < Globals.sparrow_x and not self.scored:
            Globals.SCORE += 1
            self.scored = True
            self.room.update_score()
            if (Globals.SCORE % 2) == 0:
                Globals.scroll_speed += 1
                Globals.delay_short -= 5
                Globals.delay_long -= 5

        if self.x < -80:
            self.delete_object(self)
