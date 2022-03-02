
import random

head_names = ['a', 'b', 'c', 'd']
body_names = ['e', 'f', 'g', 'h']
leg_names = ['i', 'j', 'k', 'l']
class Gear:

    def __init__(self, name, defense):

        self.name = name
        self.defense = defense

    def show_stats(self):
        print(f'name: {self.name} defense: {self.defense}')

class Armour:

    def __init__(self, head, body, legs):
        self.head = head
        self.body = body
        self.legs = legs
    def show_gear(self):
        print(f'head: {self.head.name} body: {self.body.name} leg : {self.legs.name} ')


def get_gear():

    armour = Armour(Gear(head_names[random.randint(0,3)], random.randint(1, 10)),Gear(body_names[random.randint(0,3)], random.randint(1, 10)),Gear(leg_names[random.randint(0,3)], random.randint(1, 10)))
    return armour


         



