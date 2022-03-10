import discord
from discord.ext import commands, tasks
import char
DIRECTORY_DATA = r'cogs/data.txt'
#checks if the username exists in the data
def exists(author_name):

    #this needs to check if the char exists (if not then prompts the user to create the char) else : ...
    #opens file in read mode
    file = open(DIRECTORY_DATA, 'r')
    data = file.readlines()

    for i in data:
        #finds the char of the author of the command 
        author_name_from_data = i.split('/')[0]
        
        print(author_name_from_data)
        if author_name_from_data == author_name:
            return True
    
        else:
            return False

create_char_brief = """.cc (int_amount(1-10) (dex_amount(1-10) (str_amount(1-10) (name of your character) for creating your character.)"""

class CreateChar(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self.client))
        
    
    @commands.command(aliases = ['cc', 'create'], brief = create_char_brief )
    async def create_char(self, ctx, intl, dex, stre, name):
        if exists(str(ctx.message.author)) == False:
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
                        temp_char = char.Char(intl, dex, stre, name)
                        file = open(DIRECTORY_DATA, 'a')
                        file.write(str(ctx.message.author) + '/' + name + '/'+ intl + '/' + dex + '/' + stre + '\n' )
                        file.close()
                        #reads the info in the file and stores it in data
                        #sends the data in chat
                        await ctx.send('You have succesfully created your character!')

        else:
            await ctx.send('It seems that you already have a character created. To view your character stats use the view character command(.vc)')
        
    #command to view character stats
    @commands.command(aliases = ['viewc', 'vc'])
    async def view_char(self, ctx):
        #this needs to check if the char exists (if not then prompts the user to create the char) else : ...
        #opens file in read mode
        file = open(DIRECTORY_DATA, 'r')
        data = file.readlines()

        for i in data:
            #finds the char of the author of the command 
            author_name_from_data = i.split('/')[0]
            
            print(author_name_from_data)
            if author_name_from_data == str(ctx.message.author):
                #list of string in the line split by the /
                line_list = i.split('/')
                #gets the stats for the author
                name = line_list[1]
                int_author = line_list[2]
                dex_author = line_list[3]
                str_author = line_list[4]
                #prints the data in an (embeded ) message
            #embeded player stats dict
                embed_player_stats = {
                'type': 'rich',
                'title': 'Character Stats: ',
                'fields': {'intl': [int_author, 'Intellignece'], 'str': [str_author, 'Strength'] , 'dex': [dex_author, 'Dexterity'] },
                'footer':'Character Name:' + name
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
                #footer
                embed_player_stats_msg.set_footer(text = embed_player_stats.get('footer'))
                #sends the embed to the server
                await ctx.send(embed = embed_player_stats_msg)             
            #elif str(ctx.message.author) != client.user:
            #    await ctx.send('It seems that you do not have a char. If you would like to create a char, type [' + create_char_brief + '].')

        #closes the file
        file.close()


def setup(client):
    client.add_cog(CreateChar(client))