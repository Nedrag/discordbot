

class Player:

    def __init__(self, str, int, dex) -> None:
        self.str = str
        self.int = int
        self.dex = dex
        self.hp = 100*self.str
        self.mp = 100*self.str

    def player_take_dmg(amount, player):
        player.hp -= amount
        return player.hp
    
    def player_deal_dmg(self, amount, to_who):
        to_who.hp -= amount
        return to_who.hp

    def player_dead(player):
        if player.hp == 0:
            return True
        else:
            return False


        