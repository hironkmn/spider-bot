from random import randint
import discord
from discord.ext import commands
from discord import app_commands
import os

config = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='s!', intents=intents)
tree = app_commands.CommandTree

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

@bot.command()
async def rire(ctx):
    desc="<@" + str(ctx.author.id) + "> est mort de rire."
    embed=discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url='https://c.tenor.com/wIxFiobxxbIAAAAC/john-jonah-jameson-lol.gif')
    await ctx.send(embed=embed)

@bot.command()
async def hello(ctx):
    await ctx.send('Salut')

@bot.command()
async def photo(ctx, utilisateur):
    desc="<@" + str(ctx.author.id) +"> prends en photo " + str(utilisateur)
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/aw6SxQnpLvAAAAAd/spider-man-taking-pictures.gif")
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, utilisateur):
    kisses = ["https://c.tenor.com/mVhow8EMB94AAAAC/emma-andrew.gif", "https://c.tenor.com/EPo3vP8MMD0AAAAC/spiderman-mary-jane.gif"]
    aleatoire = randint(0,len(kisses)-1)
    truekiss = kisses[aleatoire]
    desc="<@" + str(ctx.author.id) +"> embrasse " + str(utilisateur)
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=truekiss)
    await ctx.send(embed=embed)

@bot.command()
async def bully(ctx, utilisateur):
    bullies = ["https://c.tenor.com/LslUNhtr0bAAAAAC/tobey-maguire-gonna-cry.gif","https://c.tenor.com/NeSd-6B6wl4AAAAC/tu-vas-chialer-spiderman.gif"]
    aleatoire = randint(0,len(bullies)-1)
    desc = "<@" + str(ctx.author.id) + "> a décidé de faire chier " + str(utilisateur)
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=bullies[aleatoire])
    await ctx.send(embed=embed)

@bot.command()
async def dance(ctx):
  desc = "<@" + str(ctx.author.id) + "> danse comme un roi !!"
  embed = discord.Embed(description=desc, color=0xFF5733)
  embed.set_image(url="https://c.tenor.com/9qZhM0uswAYAAAAd/bully-maguire-dance.gif")
  await ctx.send(embed=embed)

@bot.command()
async def cry(ctx):
  desc = "<@" + str(ctx.author.id) + "> chiale ses grands morts."
  embed = discord.Embed(description=desc, color=0xFF5733)
  embed.set_image(url="https://ic.pics.livejournal.com/airockz69/15946583/46385/46385_900.gif")
  await ctx.send(embed=embed)

@bot.command()
async def death(ctx):
    desc = "<@" + str(ctx.author.id) + "> se retrouve à l'état de poussières..."
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/-gArcqUHlNgAAAAd/spiderman-death.gif")
    await ctx.send(embed=embed)

@bot.command()
async def wtf(ctx):
    desc = "<@"+ str(ctx.author.id) + "> se dit quoi de la fuck ????"
    embed= discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/4JVPWD8GrXkAAAAC/spider-man-shocked.gif")
    await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, utilisateur: discord.Member):
    hugs = ["https://c.tenor.com/rW4HtdpmZxAAAAAd/hug-spider-man.gif","https://c.tenor.com/gG3tX97uQaQAAAAC/spiderman-iron-man.gif", "https://c.tenor.com/CtTwr740BEsAAAAC/hug-spiderman.gif"]
    aleatoire = randint(0,len(hugs)-1)
    desc = "<@" + str(ctx.author.id) + "> serre " + utilisateur + " dans ses bras."
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=hugs[aleatoire])
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

bot.run(config)
