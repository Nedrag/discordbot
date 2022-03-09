import char 

class Player:

    def __init__(self,char: char.Char, id) -> None:
        self.char = char
        self.str = char.str 
        self.int = char.int 
        self.dex = char.dex 
        self.name = char.name 
        self.hp = 100*self.str
        self.mp = 100*self.str
        self.id = id

    def player_take_dmg(self, amount):
        self.hp -= amount
        return self.hp
    
    def player_deal_dmg(self, amount, to_who):
        to_who.hp -= amount
        return to_who.hp

    def player_dead(player):
        if player.hp == 0:
            return True
        else:
            return False


        