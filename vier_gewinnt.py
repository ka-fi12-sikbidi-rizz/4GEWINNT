import numpy as np
import random


class Player:
    """
    Represents a player in the game.
    Stores the player's number and handles their moves.
    """


    __number: int

    def __init__(self):
        """
        Creates a new player with number 0.
        """
        self.__number = 0

    def set_number(self, number: int):
        """
        Sets the player's number.
        """
        self.__number = number

    def get_number(self) -> int:
        """
        Returns the player's number.
        """
        return self.__number

    def place_coin(self, coin):
        """
        Handles placing a coin on the board.
        """
        return self.place_coin


class board:
    """
    Represents the game board.
    Handles the board display and stores all game fields.
    """

    __board: np.matrix
    __rows = 6
    __columns = 7

    def get_board(self):
        """
        Returns the current game board.
        """
        return self.__board

    def __init__(self):
        """
        Creates a new empty game board.
        Sets up all fields with their positions.
        """
        self.__board = np.zeros((self.__rows, self.__columns), dtype=field)
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__board[i, j] = field(i, j)

    def print_board(self):
        """
        Shows the current board on screen.
        Uses X for player 1 and O for player 2.
        """
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
    """
    Represents one field on the board.
    Keeps track of position and which player owns it.
    """

    __x_coordinate: int
    __y_coordinate: int
    __is_occupied: bool
    __player_on_field: int

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a new empty field at given position.
        """
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__is_occupied = False
        self.__player_on_field = 0

    def set_x_coordinate(self, x_coordinate):
        """
        Updates the field's x position.
        """
        self.__x_coordinate = x_coordinate

    def set_y_coordinate(self, y_coordinate):
        """
        Updates the field's y position.
        """
        self.__y_coordinate = y_coordinate

    def get_x_coordinate(self):
        """
        Returns the field's x position.
        """
        return self.__x_coordinate

    def get_y_coordinate(self):
        """
        Returns the field's y position.
        """
        return self.__y_coordinate

    def set_is_occupied(self, is_occupied):
        """
        Marks if the field has a coin or not.
        """
        self.__is_occupied = is_occupied

    def get_is_occupied(self):
        """
        Checks if the field has a coin.
        """
        return self.__is_occupied

    def set_player_on_field(self, player):
        """
        Sets which player owns this field.
        Also marks the field as taken.
        """
        self.__player_on_field = player
        if player != 0:
            self.__is_occupied = True

    def get_player_on_field(self):
        """
        Returns which player owns this field.
        """
        return self.__player_on_field


class game:
    """
    Controls the main game flow.
    Handles turns, moves, and checks for wins.
    """

    __players: list
    __gameboard: board
    __current_player: Player
    __computer_move: int
    __is_single_player: bool

    def __init__(self):
        """
        Sets up a new game with two players.
        Player 1 starts first.
        """
        self.__players = [Player(), Player()]
        self.__players[0].set_number(1)
        self.__players[1].set_number(2)
        self.__gameboard = board()
        self.__is_single_player = False
        self.__current_player = self.__players[0]

    def get_current_player(self):
        """
        Returns who's turn it is.
        """
        return self.__current_player

    def set_game_mode(self):
        """
        Lets player choose between computer or human opponent.
        Keeps asking until getting a valid choice.
        """
        while True:
            choice = input(
                "Do you want to play against the computer or a second player? (Type 'computer' or '2players'): ").lower()
            if choice == 'computer':
                self.__is_single_player = True
                print("You are now playing against the computer, AI will demolish you.")
                break
            elif choice == '2players':
                self.__is_single_player = False
                print("You are playing against another player, who will be the sore loser?")
                break
            else:
                print("Invalid input, read before you type! Lets try it again. Please type 'computer' or '2players'.")

    def player_input(self):
        """
        Gets the column choice from players.
        Handles both human and computer moves.
        """
        if self.get_current_player().get_number() == 1:
            while True:
                player_input = input(
                    f"Player {self.get_current_player().get_number()}, choose a column between one and seven: ")
                if player_input == "quit" or player_input == "exit":
                    print("Game over. Thanks for playing, better luck next time loser!")
                    exit()
                try:
                    column = int(player_input) - 1
                    if column < 0 or column >= 7:
                        print("Invalid input. Please choose a number between one and seven.")
                    else:
                        return column
                except ValueError:
                    print("Invalid input. Please choose a number between one and seven.")
        else:
            if self.__is_single_player:
                print(f"Computer (Player 2) is making a move.")
                return random.randint(0, 6)
            else:
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
        """
        Starts a new game.
        Shows welcome message and sets up game mode.
        """
        print("Welcome to a game of 4-WINS!")
        self.set_game_mode()
        self.__current_player = self.__players[0]

    def place_coin(self, player):
        """
        Tries to put a coin in the chosen column.
        Makes sure the move is valid.
        """
        valid = False
        while not valid:
            column = self.player_input()
            for i in range(6):
                if not self.__gameboard.get_board()[i, column].get_is_occupied() and i != 5:
                    if self.__gameboard.get_board()[i + 1, column].get_is_occupied():
                        self.__gameboard.get_board()[i, column].set_player_on_field(player)
                        valid = True
                        break
                elif i == 5 and not self.__gameboard.get_board()[i, column].get_is_occupied():
                    self.__gameboard.get_board()[i, column].set_player_on_field(player)
                    valid = True
                    break
                if i == 0 and self.__gameboard.get_board()[i, column].get_is_occupied():
                    print("The column is full, please choose another one.")
                    break

    def switch_active_player(self):
        """
        Changes turns between players.
        Switches from player 1 to 2 or back.
        """
        if self.__current_player == self.__players[0]:
            self.__current_player = self.__players[1]
        else:
            self.__current_player = self.__players[0]

    def check_win(self):
        """
        Looks for 4 coins in a row.
        Checks horizontal, vertical and diagonal lines.
        """
        matrix = self.__gameboard.get_board()
        for row in range(6):
            for col in range(4):
                current = matrix[row, col].get_player_on_field()
                if current != 0:
                    if all(current == matrix[row, col + i].get_player_on_field() for i in range(4)):
                        return current

        for row in range(3):
            for col in range(7):
                current = matrix[row, col].get_player_on_field()
                if current != 0:
                    if all(current == matrix[row + i, col].get_player_on_field() for i in range(4)):
                        return current

        for row in range(3):
            for col in range(4):
                current = matrix[row, col].get_player_on_field()
                if current != 0:
                    if all(current == matrix[row + i, col + i].get_player_on_field() for i in range(4)):
                        return current

        for row in range(3, 6):
            for col in range(4):
                current = matrix[row, col].get_player_on_field()
                if current != 0:
                    if all(current == matrix[row - i, col + i].get_player_on_field() for i in range(4)):
                        return current

        return 0

    def run_game(self):
        """
        Runs the main game loop.
        Shows board, handles moves, and checks for wins.
        """
        while True:
            self.__gameboard.print_board()
            self.place_coin(self.__current_player.get_number())
            if self.check_win():
                return False
            self.switch_active_player()

    def game_end(self):
        """
        Handles the end of the game.
        Shows final board and announces winner.
        """
        self.__gameboard.print_board()
        winner = self.check_win()

        if winner == 1 or winner == 2:
            print(f"Player {winner} has won!")
        else:
            print("Game draw, great minds think alike or so they say!")

        print("Game over. See you later alligator!")
        exit()

    def get_gameboard(self):
        """
        Returns the current game board.
        """
        return self.__gameboard


if __name__ == "__main__":
    game = game()
    game.game_start()
    while game.run_game():
        pass
    game.game_end()