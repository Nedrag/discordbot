import json




class Player:

    def __init__(self,id):
        #loads all values for the player from the player database
        self.id = id
        self.str = json_load_player(self.id)['str'] 
        self.int = json_load_player(self.id)['int'] 
        self.dex = json_load_player(self.id)['dex'] 
        self.name = json_load_player(self.id)['char_name'] 
        self.armor = 0
        self.level = 1
        self. exp = 0

        self.inventory = json_load_player(self.id)['inventory'] 
        self.gear = self.inventory['gear'] 
        self.gold = self.inventory['gold']
    
    def player_level_up(self, data = r'cogs/player_items.json'):
        with open(data, 'w') as file:
            f = json.load(file)
            temp = f['data'][self.id]
            temp['level'] += 1
            json.dump(temp, file, indent = 4, sort_keys= True)



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
    



        
def json_load_player(player_name, data = r'cogs/player_items.json'):
    with open(data, 'r+') as file: 
        f = json.load(file)
        player_dict = f['data'][player_name]['character']
    return player_dict 