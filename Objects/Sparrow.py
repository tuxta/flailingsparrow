from GameFrame import RoomObject, Globals
import pygame


class Sparrow(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.player_images = []
        self.player_images.append(self.load_image('bird1.png'))
        self.player_images.append(self.load_image('bird2.png'))
        self.player_images.append(self.load_image('bird3.png'))
        self.player_images.append(self.load_image('bird2.png'))

        self.player_images_up = []
        self.player_images_up.append(self.load_image('bird1_up.png'))
        self.player_images_up.append(self.load_image('bird2_up.png'))
        self.player_images_up.append(self.load_image('bird3_up.png'))
        self.player_images_up.append(self.load_image('bird2_up.png'))

        self.player_images_down = []
        self.player_images_down.append(self.load_image('bird1_down.png'))
        self.player_images_down.append(self.load_image('bird2_down.png'))
        self.player_images_down.append(self.load_image('bird3_down.png'))
        self.player_images_down.append(self.load_image('bird2_down.png'))

        self.set_image(self.player_images[0], 64, 64)

        self.gravity = 0
        self.handle_key_events = True
        self.register_collision_object('Ground')
        self.register_collision_object('ColumnTop')
        self.register_collision_object('ColumnBottom')

        self.GAME_OVER = False

        self.animation_count = 0

        self.animate()

    def animate(self):
        self.animation_count += 1
        self.animation_count %= 4

        if self.y_speed < -3:
            self.set_image(self.player_images_up[self.animation_count], 64, 64)
        elif self.y_speed > 8:
            self.set_image(self.player_images_down[self.animation_count], 64, 64)
        else:
            self.set_image(self.player_images[self.animation_count], 52, 52)

        if self.y < 435:
            self.set_timer(4, self.animate)
        else:
            self.set_image(self.player_images_down[2], 64, 64)

    def key_pressed(self, key):
        if key[pygame.K_SPACE] and Globals.scroll_speed != 0:
            self.set_direction(270, 8)
            self.gravity = 1

        if key[pygame.K_RETURN] and Globals.scroll_speed == 0:
            self.room.running = False
            self.y = 300
            Globals.scroll_speed = 4
            self.GAME_OVER = False
            Globals.SCORE = 0

    def step(self):
        if self.y >= 436:
            self.y = 435
            self.gravity = 0
            if not self.GAME_OVER:
                self.room.game_over()
                self.GAME_OVER = True
        elif self.y <= 0:
            self.y = 0

    def handle_collision(self, other, other_type):
        Globals.scroll_speed = 0
        if Globals.SCORE > Globals.high_score:
            Globals.high_score = Globals.SCORE
