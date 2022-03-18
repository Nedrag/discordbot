import item 
import json

"""
By gear I consider armour , it serves a pourpse of beefing up the  stats basiclly.
It`s a subclass of the Item class and all possible gear is being stored in a json file for now
gear class items id`s end with a ---1
"""

class Gear(item.Item):
    def __init__(self):
        super().__init__()
        self.intl = int(setup()[self.id]['stats'].split('.')[0])
        self.str = int(setup()[self.id]['stats'].split('.')[1])
        self.dex = int(setup()[self.id]['stats'].split('.')[2])
        self.armor = setup()[self.id]['stats']['armor']
          
def setup(data = r'items.json'):
    with open(data, 'r') as file:
        f = json.load(file)
        temp = f['data']
    return temp