import arcade

from Chapter_6.pong_game.design.colors import BG_COLOR


class Game(arcade.Window):
    def on_draw(self):
        self.clear(BG_COLOR)


def main():
    game = Game()
    arcade.run()


if __name__ == '__main__':
    main()
