import arcade

from Chapter_6.pong_game.design.dimensions import ROCKET_RATIO


class RocketSprite(arcade.Sprite):
    PICTURE_PATH = 'assets/img/rocket.png'

    def __init__(self):
        super().__init__(self.PICTURE_PATH, ROCKET_RATIO)
