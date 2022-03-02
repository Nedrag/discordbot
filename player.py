from unicodedata import name
import char as c

class Player:
    def __init__(self, id, char):

        self.id = id
        self.char = char
    
    def get_char(self, name, id, klasa, str, int, dex):
        char = c.get_char(name, klasa, str, int , dex)
        self.id = id
        return char 

def get_player(id, char):
    player = Player(char, id)

    return player

