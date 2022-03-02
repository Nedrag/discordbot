import discord
import random


TOKEN = "OTQ3ODE1NDEzNDAyNzEwMDU3.Yhyv5A.JUzxSVTzPQBOdGSQjMuQFxKyB_U"

client = discord.Client()

key_words = ['osam', 'jedan', 'dva', 'tri', 'ko','devet']
odgovori_random = {1:'Majku ti jebem!', 2:'Na kurcu te nosam!', 3:'Pusi ga majmune!', 4:'Onaj sto sam te jebao!'}

odgovori = {'jedan':'Majku ti jebem!', 'osam':'Na kurcu te nosam!', 'tri':'Pusi ga majmune!', 'ko':'Onaj sto sam te jebao!', 'dva':'jebem te ja!'}

#on_ready - kada se prikljuci serveru bot sta da radi
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#fetchuje svaku poruku na serveru
@client.event
async def on_message(message):
    #od message uzme authora i splituje gde nadje # -> dobije  samo username 
    username = str(message.author).split('#')[0]
    #fetchuje poruku
    content = str(message.content)
    #fetchuje kanal
    channel = str(message.channel.name)
    print(f'{username}: {content} ({channel})')

    #stops the inf loop
    if message.author == client.user:
        return
    #chat clear
    if content.lower() == "!purge":
        deleted = await message.channel.purge(limit = 200,bulk = True )
        await message.channel.send('CHAT IS PURGED! (Deleted {} message(s))'.format(len(deleted)))
        print(f'{message}')
        
        return
    #SVRHA SVEGA 
    if content.lower() == "!randomon":
        random_mode = True
        await message.channel.send('RANDOM MODE IS ON!')
        return
    if content.lower() == "!randomff":
        random_mode = False
        await message.channel.send('RANDOM MODE IS OFF!')
        return

    if channel == 'general':
        random_response = odgovori_random[random.randint(1,4)]

        for word in key_words:
            if content.lower() == word:
                await message.channel.send(f'{random_response}', reference = message)
                return
    if channel == 'general':
        for word in odgovori.keys():
            if content.lower() == word:
                await message.channel.send(f'{odgovori[word]}', reference = message)
                return




    

    
    




    




#pokrene bota
client.run(TOKEN)