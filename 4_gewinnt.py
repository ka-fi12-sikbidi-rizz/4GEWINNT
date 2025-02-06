import numpy as np
class Player:

    def set_symbol(self, symbol) -> None:
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.symbol



    def set_name(self, name) -> None:
        self.name = name
        

    def get_name(self) -> str:
        return self.name
    

    def __init__(self):
        self.name = ""
        self.symbol = ""
        self.coins = 21


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
                        print("▄", end=' ')
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

if __name__ == "__main__":
    b = board()
    b.get_board()[5, 3].set_player_on_field(1)
    b.get_board()[4, 3].set_player_on_field(2)
    b.print_board()