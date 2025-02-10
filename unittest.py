import unittest
from vier_gewinnt import game


class TestConnect4Game(unittest.TestCase):
    """
    Tests for the Connect 4 game.
    Checks if all game rules and moves work correctly.
    """

    def setUp(self):
        """
        Creates a new game before each test.
        """
        self.test_game = game()
        self.test_game.game_start()

    def test_initial_board_empty(self):
        """
        Checks if the game board starts empty.
        Makes sure all spots are set to 0.
        """
        gameboard = self.test_game.get_gameboard().get_board()
        for i in range(6):
            for j in range(7):
                self.assertEqual(gameboard[i, j].get_player_on_field(), 0)

    def test_place_coin(self):
        """
        Checks if a coin can be placed on the board.
        Makes sure it falls to the bottom of the column.
        """
        self.test_game.place_coin(1)
        gameboard = self.test_game.get_gameboard().get_board()

        self.assertEqual(gameboard[5, 0].get_player_on_field(), 1)
        self.assertEqual(gameboard[4, 0].get_player_on_field(), 0)

    def test_place_coin_stacking(self):
        """
        Checks if coins stack on top of each other.
        Makes sure coins from different players stack in the right order.
        """
        self.test_game.place_coin(1)
        self.test_game.place_coin(2)
        gameboard = self.test_game.get_gameboard().get_board()

        self.assertEqual(gameboard[5, 0].get_player_on_field(), 1)
        self.assertEqual(gameboard[4, 0].get_player_on_field(), 2)

    def test_vertical_win(self):
        """
        Checks if a player wins by placing 4 coins in a column.
        Tests if the game spots this type of win.
        """
        for _ in range(4):
            self.test_game.place_coin(1)

        self.assertEqual(self.test_game.check_win(), 1)

    def test_horizontal_win(self):
        """
        Checks if a player wins by placing 4 coins in a row.
        Tests if the game spots this type of win.
        """
        gameboard = self.test_game.get_gameboard().get_board()

        for i in range(4):
            gameboard[5, i].set_player_on_field(1)

        self.assertEqual(self.test_game.check_win(), 1)

    def test_diagonal_win(self):
        """
        Checks if a player wins by placing 4 coins diagonally.
        Tests if the game spots this type of win.
        """
        gameboard = self.test_game.get_gameboard().get_board()

        positions = [
            (5, 0, 2), (5, 1, 2), (5, 2, 2), (5, 3, 1),
            (4, 0, 2), (4, 1, 2), (4, 2, 1),
            (3, 0, 2), (3, 1, 1),
            (2, 0, 1)
        ]

        for row, col, player in positions:
            gameboard[row, col].set_player_on_field(player)

        self.assertEqual(self.test_game.check_win(), 1)

    def test_no_win(self):
        """
        Checks if an empty board shows no winner.
        Makes sure the game doesn't show a false win.
        """
        self.assertEqual(self.test_game.check_win(), 0)

    def test_full_column(self):
        """
        Checks what happens when a column is full.
        Makes sure the game handles full columns correctly.
        """
        gameboard = self.test_game.get_gameboard().get_board()

        for i in range(6):
            gameboard[i, 0].set_player_on_field(1)

        self.test_game.place_coin(1)

        self.assertEqual(gameboard[0, 0].get_player_on_field(), 1)

    def test_invalid_column(self):
        """
        Checks what happens when picking a wrong column number.
        Makes sure the game board doesn't change when this happens.
        """
        initial_board = self.test_game.get_gameboard().get_board()
        gameboard_state = [[initial_board[i, j].get_player_on_field()
                            for j in range(7)] for i in range(6)]

        self.test_game.place_coin(10)

        current_board = self.test_game.get_gameboard().get_board()
        for i in range(6):
            for j in range(7):
                self.assertEqual(current_board[i, j].get_player_on_field(),
                                 gameboard_state[i][j])


if __name__ == '__main__':
    unittest.main()