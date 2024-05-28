import random
from solver import Puzzle

class Game:
    def __init__(self, size=4, shuffle_steps=100):
        self.size   = size
        self.puzzle = self.create_board()
        self.empty_row, self.empty_col = self.get_empty_position()
        self.moves = 0
        self.shuffle_steps = shuffle_steps

    def create_board(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(i * self.size + j + 1)
            board.append(row)
        board[self.size - 1][self.size - 1] = 0
        return Puzzle(board)

    def get_empty_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle.board[i][j] == 0:
                    return i, j

    def shuffle_board(self):
        for _ in range(self.shuffle_steps):
            moves = self.get_valid_moves()
            random_move = random.choice(moves)
            self.move(random_move)

    def get_valid_moves(self):
        moves = []
        if self.empty_row > 0:
            moves.append('up')
        if self.empty_row < self.size - 1:
            moves.append('down')
        if self.empty_col > 0:
            moves.append('left')
        if self.empty_col < self.size - 1:
            moves.append('right')
        return moves

    def print_board(self):
        for row in self.puzzle.board:
            print(row)
        print("")

    def move(self, direction):
        if direction == "down":
            if self.empty_row == self.size - 1:
                return
            self.puzzle.board[self.empty_row][self.empty_col], self.puzzle.board[self.empty_row + 1][self.empty_col] = \
                self.puzzle.board[self.empty_row + 1][self.empty_col], self.puzzle.board[self.empty_row][self.empty_col]
            self.empty_row += 1
        elif direction == "up":
            if self.empty_row == 0:
                return
            self.puzzle.board[self.empty_row][self.empty_col], self.puzzle.board[self.empty_row - 1][self.empty_col] = \
                self.puzzle.board[self.empty_row - 1][self.empty_col], self.puzzle.board[self.empty_row][self.empty_col]
            self.empty_row -= 1
        elif direction == "right":
            if self.empty_col == self.size - 1:
                return
            self.puzzle.board[self.empty_row][self.empty_col], self.puzzle.board[self.empty_row][self.empty_col + 1] = \
                self.puzzle.board[self.empty_row][self.empty_col + 1], self.puzzle.board[self.empty_row][self.empty_col]
            self.empty_col += 1
        elif direction == "left":
            if self.empty_col == 0:
                return
            self.puzzle.board[self.empty_row][self.empty_col], self.puzzle.board[self.empty_row][self.empty_col - 1] = \
                self.puzzle.board[self.empty_row][self.empty_col - 1], self.puzzle.board[self.empty_row][self.empty_col]
            self.empty_col -= 1

    def is_solved(self):
        flattened_board = [element for row in self.puzzle.board for element in row]
        return flattened_board == list(range(1, self.size ** 2)) + [0]

    def get_state(self):
        return tuple(tuple(row) for row in self.puzzle.board)

    def set_state(self, state):
        self.puzzle.board = [list(row) for row in state]
        self.empty_row, self.empty_col = self.get_empty_position()
