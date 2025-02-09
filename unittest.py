import unittest
from vier_gewinnt import game


class TestConnect4Game(unittest.TestCase):
    def setUp(self):
        """Wird vor jedem Test ausgeführt - initialisiert ein neues Spiel"""
        self.test_game = game()
        self.test_game.game_start()

    def test_initial_board_empty(self):
        """Testet ob das Spielfeld zu Beginn leer ist"""
        gameboard = self.test_game.get_gameboard().get_board()
        for i in range(6):
            for j in range(7):
                self.assertEqual(gameboard[i, j].get_player_on_field(), 0)

    def test_place_coin(self):
        """Testet ob ein Spielstein korrekt platziert wird"""

        self.test_game.place_coin(1)
        gameboard = self.test_game.get_gameboard().get_board()

        self.assertEqual(gameboard[5, 0].get_player_on_field(), 1)

        self.assertEqual(gameboard[4, 0].get_player_on_field(), 0)

    def test_place_coin_stacking(self):
        """Testet ob Steine korrekt gestapelt werden"""

        self.test_game.place_coin(1)
        self.test_game.place_coin(2)
        gameboard = self.test_game.get_gameboard().get_board()


        self.assertEqual(gameboard[5, 0].get_player_on_field(), 1)  # Unten
        self.assertEqual(gameboard[4, 0].get_player_on_field(), 2)  # Darüber

    def test_vertical_win(self):
        """Testet ob ein vertikaler Gewinn erkannt wird"""

        for _ in range(4):
            self.test_game.place_coin(1)

        self.assertEqual(self.test_game.check_win(), 1)

    def test_horizontal_win(self):
        """Testet ob ein horizontaler Gewinn erkannt wird"""
        gameboard = self.test_game.get_gameboard().get_board()


        for i in range(4):
            gameboard[5, i].set_player_on_field(1)

        self.assertEqual(self.test_game.check_win(), 1)

    def test_diagonal_win(self):
        """Testet ob ein diagonaler Gewinn erkannt wird"""
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
        """Testet ob bei leerem Spielfeld kein Gewinner erkannt wird"""
        self.assertEqual(self.test_game.check_win(), 0)

    def test_full_column(self):
        """Testet ob eine volle Spalte korrekt erkannt wird"""
        gameboard = self.test_game.get_gameboard().get_board()


        for i in range(6):
            gameboard[i, 0].set_player_on_field(1)


        self.test_game.place_coin(1)


        self.assertEqual(gameboard[0, 0].get_player_on_field(), 1)

    def test_invalid_column(self):
        """Testet ob ungültige Spalten korrekt behandelt werden"""
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