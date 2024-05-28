import unittest
from unittest.mock import patch
from game import Game
from solver import Puzzle

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(size=3)

    def test_is_solved(self):
        solved_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.game.puzzle = Puzzle(solved_board)
        self.assertTrue(self.game.is_solved())

    def test_move(self):
        self.game.puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.game.empty_row, self.game.empty_col = 2, 2
        self.game.move('up')
        self.assertEqual(self.game.puzzle.board, [[1, 2, 3], [4, 5, 0], [7, 8, 6]])
        self.game.move('left')
        self.assertEqual(self.game.puzzle.board, [[1, 2, 3], [4, 0, 5], [7, 8, 6]])

    @patch('random.choice', side_effect=lambda x: x[0])
    def test_shuffle_board(self, mock_choice):
        initial_state = self.game.get_state()
        self.game.shuffle_board()
        new_state = self.game.get_state()
        self.assertNotEqual(initial_state, new_state)


if __name__ == '__main__':
    unittest.main()
