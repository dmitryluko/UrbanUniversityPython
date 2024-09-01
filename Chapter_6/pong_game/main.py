import arcade

from Chapter_6.pong_game.assets.sprites.rocket_sprite import RocketSprite
from Chapter_6.pong_game.design.colors import BG_COLOR
from Chapter_6.pong_game.design.dimensions import SCREEN_WIDTH_1200, SCREEN_HEIGHT_800


class Game(arcade.Window):
    SCREEN_TITLE = " -x-> Pong Game <-x-"

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rocket = RocketSprite()

    def on_draw(self):
        self.clear(BG_COLOR)
        self.rocket.draw()


def main():
    game_window = Game(
        width=SCREEN_WIDTH_1200,
        height=SCREEN_HEIGHT_800,
        title=Game.SCREEN_TITLE
    )

    arcade.run()


if __name__ == '__main__':
    main()