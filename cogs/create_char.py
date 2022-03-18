import json
import discord
from discord.ext import commands
import player as p 
PLAYER_DIRECTORY = r'cogs/player_items.json'

def user_exists(author_name, data = PLAYER_DIRECTORY):
    file= open(data, 'r+' )
    f = json.load(file)
    for i in f["data"].keys():
        if str(author_name) == i:
            return True
        else:
            False

#loads a dictionary form a json file
def json_load(data_to_load : dict, data = PLAYER_DIRECTORY):
    file = open(data, 'r+')
    f = json.load(file)
    f["data"].update(data_to_load)
    file.seek(0)
    json.dump(f, file, indent = 4, sort_keys = True)
    file.close()

#returns a requested player info as a dict
def json_get_player_info(player_name, data = PLAYER_DIRECTORY):
    with open(data, 'r+') as file:
        f = json.load(file)
        for i in f["data"].keys():
            if str(player_name) == str(i):
                player = p.Player(str(player_name))
    return player

def dict_to_string(dict):
    string = ''
    c = 0 
    for i in dict.keys():
        c += 1
        if c != len(dict) - 1:
            string += str(dict[i]) + ','
        else:
            string += str(dict[i])

        

    return string


create_char_brief = """.cc (int_amount(1-10) (dex_amount(1-10) (str_amount(1-10) (name of your character) for creating your character.)"""

class CreateChar(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))
        
    
    @commands.command(aliases = ['cc', 'create'], brief = create_char_brief )
    async def create_char(self, ctx, intl, dex, stre, name):
        if user_exists(ctx.message.author) != True:
            if int(intl) > 10 or int(intl) < 1:
                await ctx.send('Pick a number between 1 and 10 for your int!(You will have to type the whole command again!)')
            else:
                if int(stre) > 10 or int(stre) < 1:
                    await ctx.send('Pick a number between 1 and 10 for your str!')
                else:
                    if int(dex) > 10 or int(dex) < 1:
                        await ctx.send('Pick a number between 1 and 10 for your dex!')
                    else:
                        #creates a temp char profile stores it in a txt file 
                        #
                        player = p.Player(str(ctx.message.author))
                        data_to_load = { player.id:{
                            "character":{
                                "int" : int(intl),
                                "str" : int(stre),
                                "dex" : int(dex),
                                "hp" : player.hp,
                                "mp" : player.mp,
                                "char_name": player.name,
                                "level" : 1,
                                "exp" : 0,
                                "inventory" : {
                                    "gold": 100,
                                    "items": {

                                    },
                                    "gear" : {
                                        "helmet": "White Wash Cap",
                                        "body" : "Tunic",
                                        "arms" : "Empty",
                                        "legs" : "Empty",
                                        "boots" : "Leather Boots",
                                        "arm_slot1": "Empty",
                                        "arm_slot2": "Empty"

                                    }
                                    
                                }
                            }
                        
                            }
                        
                        }
                        json_load(data_to_load)
                        
                        #reads the info in the file and stores it in data
                        #sends the data in chat
                        await ctx.send('You have succesfully created your character!')

        else:
            await ctx.send('It seemsV that you already have a character created. To view your character stats use the view character command(.vc)')
        
    #command to view character stats
    @commands.command(aliases = ['viewc', 'vc'])
    async def view_char(self, ctx):
        #this needs to check if the char exists (if not then prompts the user to create the char) else : ...
        #opens file in read mode
        if user_exists(ctx.message.author) != True:
            await ctx.send(r'It doesn`t look like you have a character, if you want to create one use the  .cc command. ')
        else:
            player  = json_get_player_info(ctx.message.author)
            embed_player_stats = {
            'type': 'rich',
            'title': 'Character Stats: ',
            'fields': {'intl': [player.int, 'Intellignece'], 'str': [player.str, 'Strength'] , 'dex': [player.dex, 'Dexterity'],
            'gold': [player.gold,'Gold'], 'gear': [player.gear,'Gear'], 'inventory': [player.inventory, 'Inventory'],
            'level': [player.level, 'Level'], "exp" : [player.exp, "Experience"]},
            'footer':'Character Name:' + player.name 
            }
            #player stats embed
                #intelligence stat
            embed_player_stats_msg = discord.Embed(type = embed_player_stats.get('type'), title = embed_player_stats.get('title'), colour = 255)
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('intl')[1],
            value = embed_player_stats.get('fields').get('intl')[0], 
            inline = True)
                #strength stat
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('str')[1],
            value = embed_player_stats.get('fields').get('str')[0], 
            inline = True)
                #dexterity stat
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('dex')[1],
            value = embed_player_stats.get('fields').get('dex')[0], 
            inline = True)
                #gold amount
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('gold')[1],
            value = embed_player_stats.get('fields').get('gold')[0], 
            inline = True)
                #gold amount
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('level')[1],
            value = embed_player_stats.get('fields').get('level')[0], 
            inline = True)
                #gear
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('gear')[1],
            value = dict_to_string(embed_player_stats.get('fields').get('gear')[0]), 
            inline = True)
                #inventory
            embed_player_stats_msg.add_field(name = embed_player_stats.get('fields').get('inventory')[1],
            value = dict_to_string(embed_player_stats.get('fields').get('inventory')[0]), 
            inline = True)
            #footer
            embed_player_stats_msg.set_footer(text = embed_player_stats.get('footer'))
            #sends the embed to the server
            await ctx.send(embed = embed_player_stats_msg)             
            


def setup(client):
    client.add_cog(CreateChar(client))