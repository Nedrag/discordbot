import discord 
import random 
import board
import char
import player

TOKEN = 'OTQ4MjI5NjU1MTI5OTE1NDIy.Yh4xrw.MZHAyAYdh53XMNbNgrfgCiCwnrU'

client = discord.Client()

players = [7663]

def setup_player(id, name, klasa, str, int, dex):
    char = char.get_char(name, klasa, str, int, dex)
    players_char = player.Player(char, id)

    return players_char

def attrbs_check(message, channel):
    if channel == 'room1':
       if message >= 1 and message <= 10:
           print('pass') 
           return True
    else:
        print('111')
        return False

    






@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    ident = str(message.author).split('#')[1]
    channel = str(message.channel.name)
    content = str(message.content)

    #class choosing dialog
    play = False 
    if message.content == '!play':
        play = True    
        for i in players:
            if i == ident:
                pass
            else:
                #
                players.append(ident)
                bot_response = await message.channel.send("""Poz, setupuj svog karaktera Izaberi koliko int-a tvoj karakter hoces da ima.(1-10)
                """)
                embeded = discord.Embed(titel = 'test', description = "cao cao cao" )
                await bot_response.add_reaction('😈')


                



    if message.author == client.user:
        return
    await message.channel.send(f'{username} id: {ident}')







client.run(TOKEN)