import discord
from discord.ext import commands



class DungeonInstance(commands.Cog):

    def __init__(self, client = commands.Bot):
        super().__init__()
        self.client = client
    

def setup(client):
    client.load_extension(DungeonInstance(client))