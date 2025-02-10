import unittest
from vier_gewinnt import game


class TestConnect4(unittest.TestCase):
    """
    Tests for the Connect 4 game.
    """

    def setUp(self):
        """
        Creates a new game before each test and sets it to 2-player mode.
        """
        self.game = game()
        self.game._game__is_single_player = False

    def test_place_coin(self):
        """
        Tests if a coin can be placed correctly on the board.
        """

        self.game._game__gameboard.get_board()[5, 0].set_player_on_field(1)

        bottom_field = self.game._game__gameboard.get_board()[5, 0]
        self.assertEqual(bottom_field.get_player_on_field(), 1)
        self.assertTrue(bottom_field.get_is_occupied())

        above_field = self.game._game__gameboard.get_board()[4, 0]
        self.assertEqual(above_field.get_player_on_field(), 0)
        self.assertFalse(above_field.get_is_occupied())

    def test_vertical_win(self):
        """
        Tests if a vertical win is correctly detected.
        """

        board = self.game._game__gameboard.get_board()
        for i in range(4):
            board[5 - i, 0].set_player_on_field(1)

        winner = self.game.check_win()
        self.assertEqual(winner, 1)

    def test_horizontal_win(self):
        """
        Tests if a horizontal win is correctly detected.
        """

        board = self.game._game__gameboard.get_board()
        for col in range(4):
            board[5, col].set_player_on_field(1)

        winner = self.game.check_win()
        self.assertEqual(winner, 1)

    def test_diagonal_win(self):
        """
        Tests if a diagonal win is correctly detected.
        """
        board = self.game._game__gameboard.get_board()

        positions = [
            (5, 0, 1), (5, 1, 2), (5, 2, 2), (5, 3, 2),
            (4, 1, 1), (4, 2, 2), (4, 3, 2),
            (3, 2, 1), (3, 3, 2),
            (2, 3, 1)
        ]

        for row, col, player in positions:
            board[row, col].set_player_on_field(player)

        winner = self.game.check_win()
        self.assertEqual(winner, 1)

    def test_switch_player(self):
        """
        Tests if player switching works correctly.
        """
        initial_player = self.game.get_current_player().get_number()
        self.game.switch_active_player()
        next_player = self.game.get_current_player().get_number()

        self.assertNotEqual(initial_player, next_player)
        self.assertTrue(next_player in [1, 2])

    def test_initial_board_empty(self):
        """
        Tests if the initial board is empty.
        """
        board = self.game._game__gameboard.get_board()

        for i in range(6):
            for j in range(7):
                self.assertFalse(board[i, j].get_is_occupied())
                self.assertEqual(board[i, j].get_player_on_field(), 0)


if __name__ == '__main__':
    unittest.main()