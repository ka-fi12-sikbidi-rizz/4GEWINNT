import numpy as np

class board:
    __fields: np.matrix
    __rows = 6
    __columns = 7

    
class field:
    __x_coordinate: int
    __y_coordinate: int
    __is_occupied: bool
    def __init__(self, x_coordinate, y_coordinate):
        self.__x_coordinate = x_coordinate 
        self.__y_coordinate = y_coordinate
        self.__is_occupied = False

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
    