import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):

    def __init__(self, client):
        super().__init__()
        self.clinet = client

    #an listener for errors
    @commands.Cog.listener()
    async def on_command_error(self,ctx:commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Oops! It looks like you didn`t but enough arguments. Type in .help [command name] for more information.')


def setup(client):
    client.add_cog(ErrorHandler(client))