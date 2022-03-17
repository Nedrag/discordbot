import random as r
import json



class Enemy:
    def __init__(self, name, intl , str, dex, moves):
        self.name = name
        self.int = intl
        self.str = str
        self.dex = dex
        self.hp = 100 + int(intl)*0,2 + int(str)*0,6 + int(dex)*0,4 
        self.mp = 100 + int(intl)*0,6 + int(str)*0,2 + int(dex)*0,5 
        self.moves = moves
        

        