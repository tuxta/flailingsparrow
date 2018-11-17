from GameFrame import Level, Globals, TextObject
from Objects import Sparrow, Ground, ColumnTop, ColumnBottom, GameOverBackground
import random


class Playing(Level):
    def __init__(self, room, joysticks):
        Level.__init__(self, room, joysticks)

        self.set_background_image('background.png')

        # Add Ground and set scrolling to the left
        ground_1 = Ground(self, 0, 499)
        ground_2 = Ground(self, 800, 499)
        self.add_room_object(ground_1)
        self.add_room_object(ground_2)

        bird = Sparrow(self, Globals.sparrow_x, 300)
        self.add_room_object(bird)

        score_text = "SCORE: {}".format(Globals.SCORE)
        self.score_text = TextObject(self, 20, 20, score_text, 40)
        self.add_room_object(self.score_text)

        self.set_timer(150, self.add_column)

    def add_column(self):
        height = random.randint(150, 450)
        bottom_column = ColumnBottom(self, 800, height)
        top_column = ColumnTop(self, 800, height - 700)
        self.add_room_object(top_column)
        self.add_room_object(bottom_column)

        self.set_timer(random.randint(Globals.delay_short, Globals.delay_long), self.add_column)

    def update_score(self):
        self.score_text.text = "SCORE: {}".format(Globals.SCORE)
        self.score_text.update_text()
        pass

    def game_over(self):
        Globals.scroll_speed = 0
        Globals.delay_short = 80
        Globals.delay_long = 120

        go_bg = GameOverBackground(self, 110, 90)
        go_bg.depth = 100
        self.add_room_object(go_bg)

        game_over_text = TextObject(self, 300, 140, 'GAME OVER', 60)
        game_over_text.depth = 500
        self.add_room_object(game_over_text)

        final_score_text = "SCORE: {} HIGH SCORE: {}".format(Globals.SCORE, Globals.high_score)
        final_score_text_obj = TextObject(self, 150, 220, final_score_text, 60)
        final_score_text_obj.depth = 200
        self.add_room_object(final_score_text_obj)

        self.delete_object(self.score_text)

        press_enter_text = TextObject(self, 150, 300, "Press 'Enter' to play again", 60)
        press_enter_text.depth = 500
        self.add_room_object(press_enter_text)
