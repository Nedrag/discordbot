from __future__ import with_statement
from ast import alias
import discord
from discord.ext import commands,tasks
import player
import char
import moves
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

def get_player_id(author):
    with open(DIRECTORY_DATA, 'r') as data:
        for player in data: 

            player_name = player.split('/')[0]

            if player_name == str(author):
                author_name = player_name


    return author_name


class Game(commands.Cog):

    def __init__(self, client):
        self.client = client 
        
        self.player1 = 0 
        self.player2 = 0
        self.moves_list_off = moves.get_move_list()
        self.is_game_started = False

        self.is_player1_dead = False
        self.is_player2_dead = False
        


        
    @commands.command(aliases = ['sg', 'start'])
    async def start_game(self, ctx, *, second_player):
        #gets the char for the author of the msg
        player_char1 = get_player_from_msg(ctx.message.author)
        self.player1 = player.Player(player_char1, get_player_id(ctx.message.author)) 

        #gets the second player from the argument of the command
        player_char2  = get_player_from_msg(second_player)
        self.player2 = player.Player(player_char2, get_player_id(second_player))
        await ctx.send(self.player2.name)
        #sends the game begins msg and ticks the is_game_on check
        await ctx.send('The combat begins')
        self.is_game_started = True

        #await ctx.send(f'player1hp : {self.player1.hp}')
        #await ctx.send(f'player2hp : {self.player2.hp}')

    @commands.command()
    #combat is gonna be turnbased, so it assigns roles to each player and sees whos turn it  is
    async def move(self, ctx, move_id):
        #checks if the has started
        if self.is_game_started == False:
            await ctx.send('Game Hasn`t started yet!')
        else:
            move_exists = False
            #finds the move in the predefined move list
            for i in self.moves_list_off:
                if str(move_id) == str(i.name):
                    move_name = i.name
                    move_dmg = i.base_dmg
                    move_exists = True
            #if the move exists changes the opposing player hp by the amount of dmg 
            #the move deals and it needs to check whos who

            #player1 moves
            if move_exists and str(ctx.message.author)  == self.player1.id and self.player2.hp > 0:
                amount_dealt = self.player2.hp  - self.player2.player_take_dmg(move_dmg)
                await ctx.send(f'{self.player2.name} has taken {amount_dealt} dmg from {self.player1.name}s {move_name}')
                await ctx.send(f'{self.player2.name} has {self.player2.hp} health remaning!')
                if self.player2.hp == 0:
                    self.is_player1_dead = True
                    await ctx.send('You`ve done it you sick bastard! You`ve killed him!')
            elif self.player2.hp == 0:
                await ctx.send('What are you doing, HE`S ALREADY DEAD!')

            #player2 moves
            if move_exists and str(ctx.message.author)  == self.player2.id and self.player1.hp >0:
                amount_dealt = self.player1.hp  - self.player1.player_take_dmg(move_dmg)
                await ctx.send(f'{self.player1.name} has taken {amount_dealt} dmg from {self.player2.name}s {move_name}')
                await ctx.send(f'{self.player1.name} has {self.player1.hp} health remaning!')
                if self.player1.hp == 0:
                    self.is_player1_dead = True
                    await ctx.send('You`ve done it you sick bastard! You`ve killed him!')

            elif self.player1.hp == 0:
                await ctx.send('What are you doing, HE`S ALREADY DEAD!')
        

        


        

    




def setup(client):
    client.add_cog(Game(client))