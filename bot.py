import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
client.run('MTExMjM3MDY4NTUzNzQzMTcxMg.GGaLjx.GifIYCIqFJA4O6xG1B_q6DmmeId0FY7TxQes1E')

#MTExMjM3MDY4NTUzNzQzMTcxMg.GGaLjx.GifIYCIqFJA4O6xG1B_q6DmmeId0FY7TxQes1E
