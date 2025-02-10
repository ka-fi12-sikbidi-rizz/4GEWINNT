import unittest
from unittest.mock import patch #
from vier_gewinnt import game


class Unittest4WINS(unittest.TestCase):
    """
    Tests for the Connect 4 game.
    """

    def setUp(self):
        """
        Creates a new game before each test and sets it to 2-player mode.
        """
        self.game = game()
        self.game._game__is_single_player = False

    def test_place_coin(self, mock_input):
        """
        Checks if a coin can be placed on the board.
        """
        self.game.place_coin(1)

        board = self.game.get_gameboard().get_board()

        bottom = board[5, 0].get_player_on_field()
        self.assertEqual(bottom, 1)

        above = board[4, 0].get_player_on_field()
        self.assertEqual(above, 0)

    def test_vertical_win(self, mock_input):
        """
        Checks if a player wins by placing 4 coins in a column.
        """
        for _ in range(4):
            self.game.place_coin(1)

        winner = self.game.check_win()
        self.assertEqual(winner, 1)

    def test_horizontal_win(self):
        """
        Checks if a player wins by placing 4 coins in a row.
        """
        board = self.game.get_gameboard().get_board()

        for spalte in range(4):
            board[5, spalte].set_player_on_field(1)  # Spieler 1 legt eine Münze

        winner = self.game.check_win()
        self.assertEqual(winner, 1)

    def test_diagonal_win(self):
        """
        Checks if a player wins by placing 4 coins diagonally.
        """
        board = self.game.get_gameboard().get_board()

        positionen = [
            (5, 0, 2), (5, 1, 2), (5, 2, 2), (5, 3, 1),
            (4, 0, 2), (4, 1, 2), (4, 2, 1),
            (3, 0, 2), (3, 1, 1),
            (2, 0, 1)
        ]

        for zeile, spalte, spieler in positionen:
            board[zeile, spalte].set_player_on_field(spieler)

        winner = self.game.check_win()
        self.assertEqual(winner, 1)


if __name__ == '__main__':
    unittest.main()
