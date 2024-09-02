import arcade

from Chapter_6.pong_game.assets.sprites.rocket_sprite import RocketSprite
from Chapter_6.pong_game.design.colors import BG_COLOR
from Chapter_6.pong_game.design.dimensions import SCREEN_WIDTH, SCREEN_HEIGHT


class Game(arcade.Window):
    SCREEN_TITLE = " -x-> Pong Game <-x-"

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.rocket = RocketSprite()

        self.setup()

    def setup(self):
        self.rocket.center_x = SCREEN_WIDTH / 2
        self.rocket.center_y = SCREEN_HEIGHT / 5

    def on_draw(self):
        self.clear(BG_COLOR)
        self.rocket.draw()


def main():
    game_window = Game(
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        title=Game.SCREEN_TITLE
    )

    arcade.run()


if __name__ == '__main__':
    main()
