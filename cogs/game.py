
import random
import discord
from discord.ext import commands,tasks
import player as player
import char as char
import moves as moves
import dungeon as d
DIRECTORY_DATA = r'cogs/data.txt'

def format_dmg(dmg):
    return f'{dmg:.2f}' 



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
        self.members = []
        self.guild_roles = []
        
        self.attacker_role = 0
        self.deffender_role = 0
        self.turn_counter = 0
        
        self.enemies = []
        self.dungeon_instance = 0 
        self.dng_started = False



        
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
        #gets all the members
        self.members = await ctx.guild.fetch_members(limit = None).flatten()
        for i in self.members:
            print(i)

        #roles for adding
        self.guild_roles = await ctx.guild.fetch_roles()
        for i in self.guild_roles:
            if str(i.name) == 'atk':
                self.attacker_role = i
            if str(i.name) == 'def':
                self.deffender_role = i
        for i in self.members:
            print(i.roles)
        

        await ctx.message.author.remove_roles(self.deffender_role)
        await ctx.message.author.add_roles(self.attacker_role)
        for i in self.members:
            if str(self.player2.id) == str(i):
                await i.remove_roles(self.attacker_role)
                await i.add_roles(self.deffender_role)
            
        self.turn_counter = 1




#pvp combat
    @commands.command()
    #combat is gonna be turnbased, so it assigns roles to each player and sees whos turn it  is
    async def move(self, ctx, move_id): 
        author_role = ctx.message.author.roles[1]
        #checks if game the has started and if the author has the appropriate role
        if self.is_game_started == False:

            await ctx.send('Game Hasn`t started yet!')
        elif self.player1.hp <= 0 or self.player2.hp <= 0:
            await ctx.send('The combat has ended!')
        else:
            move_exists = False
            #finds the move in the predefined move list
            for i in self.moves_list_off.keys():
                if str(move_id) == str(i):
                    move_name = self.moves_list_off[i].name
                    move_dmg = moves.get_move_dmg(self.moves_list_off[i].base_dmg,self.player1.char.int)
                    move_exists = True
                    #move embeds
                    embed_move = discord.Embed(title = move_name, type = 'rich', colour = 100 )
                    embed_move.add_field(name = 'Damage:', value =format_dmg(move_dmg), inline = True )
            #if the move exists changes the opposing player hp by the amount of dmg 
            #the move deals and it needs to check whos who

            #player1 moves
            if move_exists and str(ctx.message.author)  == self.player1.id and self.player2.hp > 0 and author_role.name == 'atk':
                amount_dealt = self.player2.hp  - self.player2.player_take_dmg(move_dmg) 
                await ctx.send(f'{self.player2.name} has taken {amount_dealt:.2f} dmg from {self.player1.name}s {move_name}')
                await ctx.send(embed = embed_move)
                
                
                if self.player2.hp <= 0:
                    embed_move.add_field(name = f'{self.player2.name} HP: ', value= 0)
                    embed_move.add_field(name = f'{self.player1.name} HP: ', value= format_dmg(self.player1.hp))
                    self.is_player1_dead = True
                    await ctx.send(r'You`ve done it you sick bastard! You`ve killed him!')
                    await ctx.send('The combat ends')
                    
                else:
                    embed_move.add_field(name = f'Player {self.player1.name} HP: ', value = self.player1.hp, inline = True)
                    embed_move.add_field(name = f'Player {self.player2.name} HP: ', value = self.player2.hp, inline = True)
                    await ctx.send(f'{self.player2.name} has {self.player2.hp} health remaning!')
                    await ctx.message.author.remove_roles(self.attacker_role)
                    await ctx.message.author.add_roles(self.deffender_role)
                    for i in self.members:
                        if str(i) == str(self.player2.id):
                            await i.remove_roles(self.deffender_role)
                            await i.add_roles(self.attacker_role)
                    self.turn_counter += 1


            #player2 moves
            if move_exists and str(ctx.message.author)  == str(self.player2.id) and self.player1.hp >0 and author_role.name == 'atk':
                amount_dealt = self.player1.hp  - self.player1.player_take_dmg(move_dmg * 5)
                await ctx.send(f'{self.player1.name} has taken {amount_dealt} dmg from {self.player2.name}s {move_name}')
                await ctx.send(embed = embed_move)

                if self.player1.hp <= 0:
                    embed_move.add_field(name = f'{self.player1.name} HP: ', value= 0)
                    embed_move.add_field(name = f'{self.player2.name} HP: ', value= format_dmg(self.player2.hp))
                    self.is_player1_dead = True
                    await ctx.send('You`ve done it you sick bastard! You`ve killed him!')
                else:
                    embed_move.add_field(name = f'Player {self.player1.name} HP: ', value = self.player1.hp, inline = True)
                    embed_move.add_field(name = f'Player {self.player2.name} HP: ', value = self.player2.hp, inline = True)
                    await ctx.send(f'{self.player1.name} has {self.player1.hp} health remaning!')
                    await ctx.message.author.remove_roles(self.attacker_role)
                    await ctx.message.author.add_roles(self.deffender_role)
                    for i in self.members:
                        if str(i) == str(self.player1.id):
                            await i.remove_roles(self.deffender_role)
                            await i.add_roles(self.attacker_role)
                    self.turn_counter += 1
#starts the dungeon run
#dungeon runs
    @commands.command(aliases = ['start_dungeon', 'sd'])
    async def dung_run(self, ctx, dng_name):

        self.dng_started = True
        randomize = [random.randint(1, 4),random.randint(1, 4),random.randint(1, 4),random.randint(1, 4)]
       #creates an instance 
        self.dungeon_instance = d.DungeonInstance(dng_name).dng_instance  
        for i in randomize:
            await ctx.send(f'{self.dungeon_instance["enemy_weak"][i - 1]}')
        await self.dng_combat(ctx)


        
        

    @commands.command()
    async def dng_combat(self, ctx):
        if self.dng_started:
            await ctx.send(f'{self.dungeon_instance["enemy_weak"][random.randint(0, 3)]}')
            await ctx.send('Is in front of you!')
            await ctx.send('Do you want to attack it')
            



        

    @commands.command()
    async def d(self, ctx, player_move, spell):
        pass
        
    

        

        






        

        


        

    




def setup(client):
    client.add_cog(Game(client))