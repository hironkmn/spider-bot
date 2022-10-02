from random import randint
import discord
from discord.ext import commands
from discord import app_commands
import interactions
import os
import asyncio

config = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='s!', intents=intents)
client = interactions.Client(config)

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
    embed.set_image(url='https://c.tenor.com/G2FTrHXLcBMAAAAC/shrek-laughing.gif')
    await ctx.send(embed=embed)

@bot.command()
async def aide(ctx):
    await ctx.send("Salut ! C'est Shrek Bot ! L'Ogre du serveur !\nJe vois que tu galères concernant mon utilisation, voici donc l'aide !\n\n`s!rire`: te permet de montrer tes belles dents lorsque tu es en train de rire !\n`s!burp`: te permet de roter comme moi.\n`s!kiss`: te permet d'embrasser l'amour de ta vie. Comme moi avec Fiona!\n`s!bully`: te permet de bully la personne de ton choix. Parfois, je repense au jour où j'ai cassé la gueule à Charmant.\n`s!dance`: permet de montrer à tout le serveur tes talents de danseur!\n`s!cry`: te permet de pleurer. C'était mon marais...\n`s!death`: te permet de mourir. RIP Harold...\n`s!wtf`: te permet de montrer ton incompréhension. Trop vieux pour ces conneries.")

@bot.command()
async def burp(ctx, utilisateur: discord.Member):
    desc="<@" + str(ctx.author.id) +"> prends en photo " + utilisateur.mention
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://static.wikia.nocookie.net/smash_moveset_fanon/images/0/03/Shrek_flamethrower_burp.gif/revision/latest/scale-to-width-down/320?cb=20200524194602")
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, utilisateur: discord.Member):
    kisses = ["https://c.tenor.com/c0Da0EnLproAAAAC/shrek-and-fiona-love.gif", "https://thumbs.gfycat.com/ChillyHeavyDore-size_restricted.gif"]
    aleatoire = randint(0,len(kisses)-1)
    truekiss = kisses[aleatoire]
    desc="<@" + str(ctx.author.id) +"> embrasse " + utilisateur.mention
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=truekiss)
    await ctx.send(embed=embed)

@bot.command()
async def bully(ctx, utilisateur: discord.Member):
    bullies = ["https://thumbs.gfycat.com/AthleticWeirdItalianbrownbear-size_restricted.gif","https://desertcroc.files.wordpress.com/2021/02/shrek-strength.gif"]
    aleatoire = randint(0,len(bullies)-1)
    desc = "<@" + str(ctx.author.id) + "> a décidé de faire chier " + utilisateur.mention
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=bullies[aleatoire])
    await ctx.send(embed=embed)

@bot.command()
async def dance(ctx):
  desc = "<@" + str(ctx.author.id) + "> danse comme un roi !!"
  embed = discord.Embed(description=desc, color=0xFF5733)
  embed.set_image(url="https://thumbs.gfycat.com/RadiantDapperImpala-size_restricted.gif")
  await ctx.send(embed=embed)

@bot.command()
async def cry(ctx):
  desc = "<@" + str(ctx.author.id) + "> est oméga triste"
  embed = discord.Embed(description=desc, color=0xFF5733)
  embed.set_image(url="https://thumbs.gfycat.com/EducatedGiganticCanvasback-max-1mb.gif")
  await ctx.send(embed=embed)

@bot.command()
async def death(ctx):
    desc = "<@" + str(ctx.author.id) + "> donne son dernier souffle..."
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/Ls5feDO4XwYAAAAC/frog-dying-feliyfelix.gif")
    await ctx.send(embed=embed)

@bot.command()
async def wtf(ctx):
    desc = "<@"+ str(ctx.author.id) + "> se dit quoi de la fuck ????"
    embed= discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://thumbs.gfycat.com/GrippingFastCobra-size_restricted.gif")
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # do some extra stuff here
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Spider-Man: No Way Home"))
    await bot.process_commands(message)

loop = asyncio.get_event_loop()

task2 = loop.create_task(bot.start(config))
task1 = loop.create_task(client._ready())
gathered = asyncio.gather(task1, task2)
loop.run_until_complete(gathered)


##bot.run(config)
