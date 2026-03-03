
import discord
from discord.ext import commands
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


bot.run("usa il tuo token")
