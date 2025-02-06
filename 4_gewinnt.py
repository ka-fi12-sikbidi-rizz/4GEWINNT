class Player:

    """
    sets symbol for a player
    returns symbol of the player
    sets name for a player
    returns the name of a player
    player can choose name and symbol, we have 21 coins
    """

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
