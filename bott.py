
import discord
from discord.ext import commands
import random
import os




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

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def salve(ctx, nome = "pincopallino"):
    await ctx.send(f"ciao {nome}")

@bot.command()
async def pin(ctx, noe = 10):
    await ctx.send(gen_pass(noe))

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)   


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)



@bot.command()
async def meme(ctx):
    with open("meme1.png","rb") as f:
        discord_file=discord.File(f)
        await ctx.send(file=discord_file)

@bot.command()
async def c_meme(ctx):
    listameme=os.listdir("meeme")
    rmeme=random.choice(listameme)
    with open(f"meeme/{rmeme}","rb") as f:
        discord_file=discord.File(f)
        await ctx.send(file=discord_file)








bot.run("inserisci il tuo token")





bot.run("usa il tuo token")
