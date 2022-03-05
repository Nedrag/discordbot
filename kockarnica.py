import discord 
from discord.ext import commands
import random 
import board
import char
import player

TOKEN = ''

client = commands.Bot(command_prefix = '.')


    






@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))



@client.command()
async def clear(ctx):
    deleted = await ctx.message.channel.purge(limit = 200)
    await ctx.send(f'Deleted {len(deleted)} message(s)')


@client.listen()
async def on_message(message):
    print('one')









client.run(TOKEN)