from discord.ext import commands
import time
import datetime
import random
from googlesearch import search 
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! Katze bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Katze bot is ready!")

@bot.event
async def on_ready2():
    print("Hahaha! amazing!")
    channel = bot.get_channel(CHANNEL_ID2)
    await channel.send("Hahaha Amazing, The Katze Bot is Ready")

@bot.command()
async def dice(ctx, x):
    result = random.randint(1, 6) * int(x)
    xmult6result = (6) * int(x)
    await ctx.send(f"{result} (1 ~ {xmult6result})")

@bot.command()
async def RandNum(ctx, x, y):
    RN = random.randint(int(x), int(y))
    await ctx.send(f"{RN} ({x} ~ {y})")

@bot.command()
async def Kong(ctx):
    await ctx.send("Jinho KongJinho 22")

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
async def squ(ctx, x, y):
    result = int(x) ** int(y)
    await ctx.send(f"{x} ** {y} = {result}")

@bot.command()
async def root(ctx, x):
    result = int(x) ** (1 / 2)
    await ctx.send(f"root {x} = {result}")

@bot.command()
async def nroot(ctx, x, n):
    result = int(x) ** (1 / int(n))
    await ctx.send(f"{n}root {x} = {result}")

@bot.command()
async def Whatareyoudoing(ctx):
    await ctx.send("I'm coding my self")

@bot.command()
async def GarticPhone(ctx):
    await ctx.send("Come Join Us! https://garticphone.com/ko/lobby")

@bot.command()
async def Kkutu(ctx):
    await ctx.send("Come Join Us! https://kkutu.co.kr/")

@bot.command()
async def Hi(ctx):
    await ctx.send("Hello!")

@bot.command()
async def Hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def Nicetomeetyou(ctx):
    await ctx.send("Nice to meet you too!")

@bot.command()
async def Hahaha(ctx):
    await ctx.send("Amazing!")

@bot.command()
async def Good(ctx):
    await ctx.send("Thanks")

@bot.command()
async def Help(ctx):
    await ctx.send("Yesn't")

@bot.command()
async def fyou(ctx):
    await ctx.send("丄ㅗ凸ㅗ丄")

@bot.command()
async def CallAll(ctx):
    await ctx.send("@everyone")

@bot.command()
async def DeveloperGmail(ctx):
    await ctx.send("kgm081024@gmail.com")

@bot.command()
async def Search(ctx, *, query):
    author = ctx.author.mention
    await ctx.send(f"Search Results for You! {author}")
    print(f"Searching {author}, {query}")
    async with ctx.typing():
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            
            await ctx.send(f"\n=>  {j}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(907580163980668962)
    embed = discord.Embed(title = "Nice to meet You!", description=f"{member.mention} Just Joined")
    await channel.send(embed = embed)

bot.run(BOT_TOKEN)
