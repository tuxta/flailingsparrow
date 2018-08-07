from GameFrame import RoomObject


class GameOverBackground(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image('game_over_bg.png')
        self.set_image(image, 300, 200)
