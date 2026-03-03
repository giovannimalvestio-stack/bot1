import discord
import random

def gen_pass(lunghezza):
        caratteri="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        passorword=""
        for i in range(lunghezza):
            passorword+=random.choice(caratteri)
        return passorword





# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('你好'):
        await message.channel.send("\我很好，你呢")
    elif message.content.startswith('password'):
        password=gen_pass(10)
        await message.channel.send(password)
    else:
        await message.channel.send(message.content)
     




client.run("il mio token")
