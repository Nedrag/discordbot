from __future__ import with_statement
import discord
from discord.ext import commands,tasks
import player
import char
DIRECTORY_DATA = r'cogs/data.txt'


def get_player_from_msg(author):
    file = open(DIRECTORY_DATA, 'r')
    data = file.readlines()
    for player in data:
        player_name = player.split('/')[0]

        if player_name == str(author):

            player_int =  int(player.split('/')[2])
            player_str =  int(player.split('/')[3])
            player_dex =  int(player.split('/')[4])
            player_nick = player.split('/')[1]

            player_char = char.Char(player_int, player_str, player_dex, player_nick ) 
    file.close()
    return player_char




class Game(commands.Cog):

    def __init__(self, client):
        self.client = client 
        
        self.player1 = 0 
        self.player2 = 0
        


        
    @commands.command()
    async def start_game(self, ctx):
        player_char = get_player_from_msg(ctx.message.author)
        self.player1 = player.Player(player_char.str, player_char.int, player_char.dex)        
        self.player2 = player.Player(10,10, 10)
        await ctx.send('The combat begins')

        #await ctx.send(f'player1hp : {self.player1.hp}')
        #await ctx.send(f'player2hp : {self.player2.hp}')

    @commands.command()
    async def move(self, ctx, move_id):
        pass

        

        

    




def setup(client):
    client.add_cog(Game(client))