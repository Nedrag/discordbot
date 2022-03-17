import json
CLASS_MULTIPLIER = 3.14/3

class Move():

    def __init__(self, base_dmg, type, name) -> None:
        self.base_dmg = base_dmg
        self.type = type
        self.name = name



moves_off = {} 
moves_json = open(r'cogs/data.json')
f = json.load(moves_json)

for i in f["moves"]:
    
    moves_off[i["move_id"]] = Move(i["move_base_dmg"], i["move_type"], i["move_name"])

moves_json.close()
for i in moves_off.keys():
    print(moves_off[i].name)




def print_moves():
    for i in moves_off:
        print(f'name: {i.name}type: {i.type}base damage: {i.base_dmg}')

def get_move_dmg(base : int, attribute: int):

    return base * CLASS_MULTIPLIER 
    

def get_move_list():
    return moves_off




    