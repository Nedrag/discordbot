import discord
import os
from discord.ext import commands

#token
token_file = open('token.txt', 'r')
token = token_file.read()
#
intents_all = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents = intents_all) 

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        client.load_extension(f'cogs.{i[:-3]}')



client.run(token)



