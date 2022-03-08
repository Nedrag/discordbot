
import char
import player as p

class Combat:

    def __init__(self, player1, player2):
        self.turn_counter = 1
        self.player1 = player1#char1
        self.player2 = player2#char2
        self.p1 = p.Player(player1.str, player1.int, player1.dex)
        self.p2 = p.Player(player2.str, player2.int, player2.dex)


    def attack(self, move):
        dmg_dealt = self.p2.hp - self.p1.player_deal_dmg(move, self.p2)
        self.turn_counter += 1
        return dmg_dealt

    def skip_turn(self):
        pass

    def end_of_combat(self):
        pass


c1 = char.Char(10, 10, 10, 'pedja')
c2 = char.Char(10, 10, 10, 'pedja')
combat = Combat(c1, c2)     

'''
test case
print(combat.p1.hp)
print(combat.p2.hp)
combat.attack(12)
combat.attack(12)
combat.attack(12)
print(combat.p1.hp)
print(combat.p2.hp)
'''


