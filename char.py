import gear

class Char:

    def __init__(self, name, klasa, str, int, dex, inventory):
        self.name = name
        self.klasa = klasa
        self.str = str
        self.int = int
        self.dex = dex
        self.inventory = inventory
        

    def show_stats(self):
        print(f'name : {self.name} str: {self.str} int: {self.int} dex: {self.dex}')
    def show_inv(self):
        for i in self.inventory.keys():
            print(f'{i}: {self.inventory[i]}\n')

def get_char(name, klasa, str, int, dex):
    inventory = {'gold': 0, 
    'head': gear.get_gear().head.name,
    'body': gear.get_gear().body.name,
    'legs': gear.get_gear().legs.name
    }
    char = Char(name, klasa, str, int, dex, inventory)
    return char 

