import enemy as en
import random as r


class DungeonInstance:
    def __init__(self, dungeon_name):
        #weak
        self.dng_instance = en.get_dung_inst(dungeon_name)
        self.level = 1


        
    def dng_level_up(self):
        self.level += 1

    
