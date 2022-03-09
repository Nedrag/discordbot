
class Move():

    def __init__(self, base_dmg, type, name) -> None:
        self.base_dmg = base_dmg
        self.type = type
        self.name = name


moves_off = [Move(100, 'str', 1), Move(100, 'int', 2), Move(100, 'dex', 3)]

def print_moves():
    for i in moves_off:
        print(f'name: {i.name}type: {i.type}base damage: {i.base_dmg}')
    

def get_move_list():
    return moves_off




    