from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
@bot.event
async def on_ready():
    print("Hello! Katze bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Katze bot is ready!")

@bot.command()
async def whatareyoudoing(ctx):
    await ctx.send("Nothing")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def Hi(ctx):
    await ctx.send("Hi!")

@bot.command()
async def Bye(ctx):
    await ctx.send("Good Bye!")

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")

@bot.command()
async def sub(ctx, x, y):
    result = int(x) - int(y)
    await ctx.send(f"{x} - {y} = {result}")

@bot.command()
async def mult(ctx, x, y):
    result = int(x) * int(y)
    await ctx.send(f"{x} * {y} = {result}")

@bot.command()
async def div(ctx, x, y):
    result = int(y) / int(x)
    await ctx.send(f"{y} / {x} = {result}")

@bot.command()
async def hahaha(ctx):
    await ctx.send("Amazing!")

@bot.command()
async def whatcanyoudo(ctx):
    await ctx.send("I can do anything soon")

@bot.command()
async def good(ctx):
    await ctx.send("Thank you!")

@bot.command()
async def Help(ctx):
    await ctx.send("Nope")

@bot.command()
async def gangmin(ctx):
    await ctx.send("Handsome Man")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
