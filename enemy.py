import random as r
import json
INT_MULT = 0.5
DEX_MULT = 0.5
STR_MULT = 0.5


enemy_types = ['weak', 'miniboss', 'boss']

class Enemy:
    def __init__(self, name):
        self.name = name

class WeakEnemy(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.int = r.randint(1, 3)
        self.dex = r.randint(1, 3)
        self.str = r.randint(1, 3)
        self.type = enemy_types[0]
        self.base_dmg = 60 + self.int * INT_MULT + self.dex * DEX_MULT + self.str * STR_MULT 
        

class MinibossEnemy(Enemy):
    def __init__(self, name):
        super().__init__(name) 
        self.int = r.randint(6, 8)
        self.dex = r.randint(6,8)
        self.str = r.randint(6,8)
        self.type = enemy_types[1]
        self.base_dmg = 90 + self.int * INT_MULT + self.dex * DEX_MULT + self.str * STR_MULT 

class BossEnemy(Enemy):
    def __init__(self, name):
        super().__init__(name) 
        self.int = r.randint(9, 10)
        self.dex = r.randint(9, 10)
        self.str = r.randint(9, 10)
        self.type = enemy_types[2] 
        self.base_dmg = 120 + self.int * INT_MULT + self.dex * DEX_MULT + self.str * STR_MULT 

        
def get_dung_inst(dung_name):
    data = open(r'cogs/data.json')
    f = json.load(data)
    for i in f["dungeons"][dung_name]:
        for x in f["dungeons"][dung_name][i]:
            print(x)
            dng_inst = f["dungeons"][dung_name]
    data.close()
    return dng_inst

get_dung_inst("ragefire_chasm") 

        

        