import discord
from discord.ext import commands
import json
import player
""" Dungeons are going to be formated like so:
1. Every dungeon gets a dedicated text channel in  witch
 multiple people can participate to kill the boss and the thrash mobs
2. Loot will be shared amongst the people who finished the dungeon
and it will be shared based on the %dmg dealt to the whole dungeon, thrash mobs and boss

What it needs to do:
-track how much dmg each player has dealt
-track who dealt the dmg
-about 2 or 3 thrash mob rounds and then the final boss fight
-specific loot for each unique dungeon
"""

def json_get_dng(name, data = r'cogs/data.json'):
    with open(data, 'r+') as file:
        f = json.load(file)
        dng = {}
        f['dungeons'][name] = dng
    return dng

def json_keep_track(name, dmg, data = r'cogs/raid_log.json'):
    with open(data, 'w+') as file:
        f = {}
        f[str(name)] = dmg

        json.dump(f, data, indent = 4, sort_keys=True)
    




class DungeonInstance(commands.Cog):

    def __init__(self, client = commands.Bot):
        super().__init__()
        self.client = client
        
        self.raid_channels = ['Ragefire Chasm']

        #Ragefire Chasm
        self.rfc_data = json_get_dng("ragefire_chasm")
        self.rfc_name = self.rfc_data["name"]
        self.rfc_loot = self.rfc_data["loot"]
        self.rfc_level_req = self.rfc_data["level_req"]
        self.rfc_spawns = self.rfc_data["enemy_weak"]
        self.rfc_mb_spaw = self.rfc_data["enemy_miniboss"]
        self.rfc_boss = self.rfc_data["enemy_boss"]
        self.rfc_channel = self.raid_channels[0] 
        self.rfc_spawntime = 0


        

    
    @commands.command()
    async def attack(self, ctx):
        for i in self.raid_channels:
            if i == str(ctx.message.channel):
                pass

                

def setup(client):
    client.load_extension(DungeonInstance(client))

