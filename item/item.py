
import json

"""
The item class represents any item that can be found in the game
"""

class Item:
    def __init__(self, id):
        self.id = id 
        self.name = setup()[str(id)]['name'] 
        self.price = setup()[str(id)]['price']
        
def setup(data = r'items.json'):
    with open(data, 'r+') as file:
        f = json.load(file)
        temp = f['data']
        
    return temp 
