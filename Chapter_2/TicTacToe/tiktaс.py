import json
import os
import pyfiglet
import random
from json.decoder import JSONDecodeError
from rich import traceback
from subprocess import call


def game_banner():
    ascii_banner = pyfiglet.figlet_format("Tic-Tac-Toe")
    print(ascii_banner)


class Board:
    def __init__(self):
        self.positions = [' ' for _ in range(10)]

    @staticmethod
    def clear_screen():
        _ = call('clear' if os.name == 'posix' else 'cls')

    def redraw(self):
        self.clear_screen()
        game_banner()
        h_line = '---+---+---'
        v_line = '|'
        print(f' {self.positions[7]} {v_line} {self.positions[8]} {v_line} {self.positions[9]}')
        print(h_line)
        print(f' {self.positions[4]} {v_line} {self.positions[5]} {v_line} {self.positions[6]}')
        print(h_line)
        print(f' {self.positions[1]} {v_line} {self.positions[2]} {v_line} {self.positions[3]}')

    def get_current_frame(self):
        return self.positions.copy()

    def is_free(self, pos):
        return self.positions[pos] == ' '

    def set_board_positions(self, pos_arr):
        self.positions = pos_arr

    def is_full(self):
        return True if ' ' not in set(self.positions[1:9]) else False

    def clear(self):
        self.positions = [' ' for _ in range(10)]


class Player:
    marker = ()
    score = {

    }

    def __init__(self, name='Human', human_mode=True):
        self.human_mode = human_mode
        self.name = name if human_mode else 'Computer'
        self.set_mark()

    def save_data(self):
        json.dump(
            self.score,
            open('db/scores.json', 'w', encoding="utf-8"),
            indent=2,
            ensure_ascii=False,
        )

    def load_data(self):
        if not os.path.exists('db'):
            os.makedirs('db')

        try:
            self.score = json.load(open('db/scores.json', 'r'))
        except FileNotFoundError:
            open('db/scores.json', 'a').close()
        except JSONDecodeError:
            print('Some thing wrong with score database! Repaired.')
            open('db/scores.json', 'w').close()

    def save_score(self, win=0, loose=0):
        cur_score = self.score.setdefault(self.name, [0, 0])
        cur_score[0] += win
        cur_score[1] += loose
        self.score[self.name] = cur_score

    def set_mark(self):
        try:
            if self.human_mode:
                while (tmp_marker := input('Enter your SIGN ( X or 0 ) -> ').upper()) not in ('0', 'X'):
                    print('Only "X" or "0" possible. Try again...')
                Player.marker = (tmp_marker, '0' if tmp_marker == 'X' else 'X')
            else:
                print(f'Computer SIGN is: {Player.marker[1]}\n')
        except IndexError:
            print(f'You have to call Human init before .')

    def get_mark(self):
        return Player.marker[0] if self.human_mode else Player.marker[1]


class Game:
    WIN_POSITIONS = [
        [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1], [7, 8, 9]
    ]
    MOVEMENTS = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

    def __init__(self):
        game_banner()
        self.board = Board()
        self.human_player = Player(input('Enter your nick -> '))
        self.ai_player = Player(human_mode=False)
        self.turn = None
        self.is_playing = False

    def first_move(self):
        if random.randint(0, 1):
            return self.ai_player
        else:
            return self.human_player

    def set_move(self, new_position, board=None, player=None):
        if not board:
            board = self.board
        if not player:
            player = self.turn
        board.positions[new_position] = player.get_mark()

    def is_winner(self, board=None):
        if not board:
            board = self.board
        for combination in self.WIN_POSITIONS:
            seq = set([board.positions[item] for item in combination])
            if (len(seq) == 1) and (' ' not in seq):
                return True
        return False

    def engage_human_move(self):
        while (move := input('\nYour next move ( 1-9 ) -> ')) not in self.MOVEMENTS or \
                not self.board.is_free(int(move)):
            print('Illegal move! Try again ...')
        return int(move)

    def get_random_move(self, moves_arr):
        legal_moves = []
        for board_cell in moves_arr:
            if self.board.is_free(board_cell):
                legal_moves.append(board_cell)
        return random.choice(legal_moves) if legal_moves else None

    def engage_ai_move(self):
        tmp_board = Board()

        for move in range(1, 10):
            tmp_board.set_board_positions(self.board.get_current_frame())
            if tmp_board.is_free(move):
                self.set_move(move, tmp_board)
                if self.is_winner(tmp_board):
                    return move

        for move in range(1, 10):
            tmp_board.set_board_positions(self.board.get_current_frame())
            if tmp_board.is_free(move):
                self.set_move(move, tmp_board, self.human_player)
                if self.is_winner(tmp_board):
                    return move

        if move := self.get_random_move([1, 3, 7, 9]):
            return move

        if self.board.is_free(5):
            return 5

        return self.get_random_move([2, 4, 6, 8])

    def show_score(self):
        score_banner = pyfiglet.figlet_format("H I G H  S C O R E ")
        print(score_banner)
        for name, score in self.human_player.score.items():
            print(f'Name: {name:<20}    WIN: {score[0]:^}  LOOSE: {score[1]:^}')

    def __turn_exec(self, move):

        self.set_move(move)
        if self.is_winner():
            self.board.redraw()
            print(f'\n{self.turn.name} WON !!!')
            if self.turn.human_mode:
                self.human_player.save_score(1, 0)
            else:
                self.human_player.save_score(0, 1)
            self.is_playing = False
        else:
            if self.board.is_full():
                self.board.redraw()
                print('\nOps! DRAW !!!')
                return False
            else:
                return True

    def loop(self):
        while True:
            self.turn = self.first_move()
            print(f'\n{self.turn.name} moves first!')
            self.is_playing = True
            while self.is_playing:
                if self.turn.human_mode:
                    self.board.redraw()
                    if not self.__turn_exec(self.engage_human_move()):
                        break
                    self.turn = self.ai_player
                else:
                    if not self.__turn_exec(self.engage_ai_move()):
                        break
                    self.turn = self.human_player

            self.show_score()
            while (choice := input('\nPlay again ? ( y / n) ').lower()) not in ('y', 'n'):
                print(f'y/n possible answer.')
            if choice == 'y':
                self.board.clear()
            else:
                break


def main():
    print ( 'Это просто строка !' )
    game = Game()
    game.human_player.load_data()
    game.loop()
    game.board.clear_screen()
    game.human_player.save_data()


if __name__ == '__main__':
    traceback.install()
    main()
