import discord
from discord.ext import commands
from bot_token import token
from parola_olustur import parola_olustur

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
  await ctx.send("\U0001f642")

@bot.command()
async def parola_ver(ctx, parola_uzunlugu=8):
    parola = parola_olustur(parola_uzunlugu)
    await ctx.send("Sizin için oluşturulan parola: " + parola)

bot.run(token)