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
async def aide(ctx):
    await ctx.send("Salut ! C'est Spider-Bot ! L'araignée sympa du serveur !\nJe vois que tu galères concernant mon utilisation, voici donc l'aide <:spiderfight:id> !\n\n`s!rire`: te permet de montrer tes belles dents lorsque tu est en train de rire !\n`s!photo`: te permet de prendre ton/ta crush en photo. Tu te débrouilles avec la justice par la suite...\n`s!kiss`: te permet d'embrasser l'amour de ta vie... ou t'es juste un grand malade mental.\n`s!bully`: te permet de bully la personne de ton choix... Cela me rappelle mes années de fac avec Flash Thompson...\n`s!dance`: permet de montrer à tout le serveur tes talents de danseurs! Je préfère qu'on évite de parler de cette scène...\n`s!cry`: te permet de pleurer. C'est les émotions comme dirait un grand footballeur...\n`s!death`: te permet de mourir. Adieu monde cruel...\n`s!wtf`: te permet de montrer ton incompréhension. On est d'jeuns donc on dit ouate ze feuk!\n`s!hug`: te permet de faire un calîn à la personne de ton choix. J'espère juste que tu tiens pas une pancarte free hugs à la Japan Expo...")

@bot.command()
async def photo(ctx, utilisateur: discord.Member):
    desc="<@" + str(ctx.author.id) +"> prends en photo " + utilisateur.mention
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url="https://c.tenor.com/aw6SxQnpLvAAAAAd/spider-man-taking-pictures.gif")
    await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, utilisateur: discord.Member):
    kisses = ["https://c.tenor.com/mVhow8EMB94AAAAC/emma-andrew.gif", "https://c.tenor.com/EPo3vP8MMD0AAAAC/spiderman-mary-jane.gif"]
    aleatoire = randint(0,len(kisses)-1)
    truekiss = kisses[aleatoire]
    desc="<@" + str(ctx.author.id) +"> embrasse " + utilisateur.mention
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=truekiss)
    await ctx.send(embed=embed)

@bot.command()
async def bully(ctx, utilisateur: discord.Member):
    bullies = ["https://c.tenor.com/LslUNhtr0bAAAAAC/tobey-maguire-gonna-cry.gif","https://c.tenor.com/NeSd-6B6wl4AAAAC/tu-vas-chialer-spiderman.gif"]
    aleatoire = randint(0,len(bullies)-1)
    desc = "<@" + str(ctx.author.id) + "> a décidé de faire chier " + utilisateur.mention
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
    desc = "<@" + str(ctx.author.id) + "> serre " + utilisateur.mention + " dans ses bras."
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=hugs[aleatoire])
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

bot.run(config)
