import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.n = 3

    def create_board(self):
        '''
        this method creates an empty board filled with -
        :return:
        full board
        '''
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('-')
            self.board.append(row)