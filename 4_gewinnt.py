import numpy as np


class Player:

    def set_number(self, number: int):
        self.number = number

    def get_number(self) -> int:
        return self.get_number()

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
            print(i+1,"║", end=' ')
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
    
    def player_input(self, current_player):
        while True:
            
            self.__gameboard.print_board()

            try:
                
                column = int(input(f"Player {current_player.get_number()}, choose a column between one and seven: ")) - 1

                
                if column < 0 or column >= 7:
                    print("Invalid input. Please choose a number between one and seven.")
                    continue

               
                if current_player.place_coin(column, self.__gameboard):
                    print(f"Player {current_player.get_number()} has set a coin in column {column + 1}.")
                else:
                    print("The row is full, please choose another one.")
                    continue

                
                if current_player == self.__players[0]:
                    current_player = self.__players[1]
                else:
                    current_player = self.__players[0]

            except ValueError:
                print("Invalid input. Please choose a number between one and seven.")

    def game_start(self):
        print("Welcome to a game of 4-WINS!")
        print("You are currently playing against another player.")

        self.__current_player = self.__players[0]


    def place_coin(self, player, column):
        for i in range(6):
            if (self.__gameboard.get_board()[i, column].get_is_occupied() == False) and (i != 5):
                if(self.__gameboard.get_board()[i+1, column].get_is_occupied() == True):
                    self.__gameboard.get_board()[i, column].set_player_on_field(player)
                    return True
            elif i == 5:
                self.__gameboard.get_board()[i, column].set_player_on_field(player)
                return True
        return False
    #def switch_active_player(self) # kati
    #def check-win(self) # Tim
    #def run_game(self) # Tim
    #def game_end(self) # kati

    def get_gameboard(self):
        return self.__gameboard

if __name__ == "__main__":
    game = game()
    b = game.get_gameboard()
    b.get_board()[5, 3].set_player_on_field(1)
    
    
    b.get_board()[4, 3].set_player_on_field(2)
    b.print_board()
    
    
