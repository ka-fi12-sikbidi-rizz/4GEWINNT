import numpy as np


class Player:
    __number: int

    def __init__(self):
        self.__number = 0

    def set_number(self, number: int):
        self.__number = number

    def get_number(self) -> int:
        return self.__number

    def place_coin(self, coin):
        return self.place_coin


class board:
    __board: np.matrix
    __rows = 6
    __columns = 7

    def get_board(self):
        return self.__board

    def __init__(self):
        self.__board = np.zeros((self.__rows, self.__columns), dtype=field)
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__board[i, j] = field(i, j)

    def print_board(self):
        for i in range(self.__rows):
            print(i + 1, "║", end=' ')
            for j in range(self.__columns):
                if field.get_is_occupied(self.__board[i, j]):
                    if self.__board[i, j].get_player_on_field() == 1:
                        print("X", end=' ')
                    else:
                        print("O", end=' ')
                else:
                    print(" ", end=' ')
            print("║")
        print("  ╚═══════════════╝")
        print("    1 2 3 4 5 6 7")


class field:
    __x_coordinate: int
    __y_coordinate: int
    __is_occupied: bool
    __player_on_field: int

    def __init__(self, x_coordinate, y_coordinate):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__is_occupied = False
        self.__player_on_field = 0

    def set_x_coordinate(self, x_coordinate):
        self.__x_coordinate = x_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.__y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.__x_coordinate

    def get_y_coordinate(self):
        return self.__y_coordinate

    def set_is_occupied(self, is_occupied):
        self.__is_occupied = is_occupied

    def get_is_occupied(self):
        return self.__is_occupied

    def set_player_on_field(self, player):
        self.__player_on_field = player
        if player != 0:
            self.__is_occupied = True

    def get_player_on_field(self):
        return self.__player_on_field


class game:
    __players: list
    __gameboard: board
    __current_player: Player

    def __init__(self):
        self.__players = [Player(), Player()]
        self.__players[0].set_number(1)
        self.__players[1].set_number(2)
        self.__gameboard = board()

    def get_current_player(self):
        return self.__current_player

    def player_input(self):
        while True:
            player_input = input(
                f"Player {self.get_current_player().get_number()}, choose a column between one and seven: ")
            if player_input == "quit" or player_input == "exit":
                print("Game over. Thanks for playing!")
                exit()
            try:
                column = int(player_input) - 1
                if column < 0 or column >= 7:
                    print("Invalid input. Please choose a number between one and seven.")
                else:
                    return column


            except ValueError:
                print("Invalid input. Please choose a number between one and seven.")

    def game_start(self):
        print("Welcome to a game of 4-WINS!")
        print("You are currently playing against another player.")

        self.__current_player = self.__players[0]

    def place_coin(self, player):
        valid = False
        while not valid:
            column = self.player_input()
            for i in range(6):
                if (self.__gameboard.get_board()[i, column].get_is_occupied() == False) and (i != 5):
                    if (self.__gameboard.get_board()[i + 1, column].get_is_occupied() == True):
                        self.__gameboard.get_board()[i, column].set_player_on_field(player)
                        valid = True
                        break
                elif i == 5 and self.__gameboard.get_board()[i, column].get_is_occupied() == False:
                    self.__gameboard.get_board()[i, column].set_player_on_field(player)
                    valid = True
                    break
                if i == 0 and self.__gameboard.get_board()[i, column].get_is_occupied() == True:
                    print("The row is full, please choose another one.")

    def switch_active_player(self):
        if self.__current_player == self.__players[0]:
            self.__current_player = self.__players[1]
        else:
            self.__current_player = self.__players[0]

    def check_win(self):
        matrix = self.__gameboard.get_board()

        for row in range(6):
            for col in range(4):
                current = board[row, col].get_player_on_field()
                if current != 0:
                    next1 = matrix[row, col + 1].get_player_on_field()
                    next2 = matrix[row, col + 2].get_player_on_field()
                    next3 = matrix[row, col + 3].get_player_on_field()
                    if current == next1 == next2 == next3:
                        return current

        for row in range(3):
            for col in range(7):
                current = matrix[row, col].get_player_on_field()
                if current != 0:
                    next1 = matrix[row + 1, col].get_player_on_field()
                    next2 = matrix[row + 2, col].get_player_on_field()
                    next3 = matrix[row + 3, col].get_player_on_field()
                    if current == next1 == next2 == next3:
                        return current
        return 0

    def run_game(self):  # Tim
        while True:
            self.__gameboard.print_board()
            self.place_coin(self.__current_player.get_number())
            if self.check_win():
                return False
            self.switch_active_player()

    def game_end(self):
        self.__gameboard.print_board()
        winner = self.check_win()

        if winner == 1 or winner == 2:
            print(f"Player {winner} has won! Congratulations!")
        else:
            print("Game draw!")

        print("Game over. Thanks for playing!")
        exit()

    def get_gameboard(self):
        return self.__gameboard


if __name__ == "__main__":
    game = game()
    game.game_start()
    while game.run_game():
        pass
    game.game_end()


