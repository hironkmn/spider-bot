from random import randint
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='s!', intents=intents)

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
    aleatoire = str(randint(0,1))
    kisses = {"0":"https://i.pinimg.com/originals/03/2e/e7/032ee7d141e317b39e3f916fffc886c4.gif", "1":"https://c.tenor.com/EPo3vP8MMD0AAAAC/spiderman-mary-jane.gif"}
    truekiss = kisses[aleatoire]
    desc="<@" + str(ctx.author.id) +"> embrasse " + str(utilisateur)
    embed = discord.Embed(description=desc, color=0xFF5733)
    embed.set_image(url=truekiss)
    await ctx.send(embed=embed)

@bot.command()
async def bully(ctx, utilisateur):
  desc = "<@" + str(ctx.author.id) + "> a décidé de faire chier " + str(utilisateur)
  embed = discord.Embed(description=desc, color=0xFF5733)
  embed.set_image(url="https://c.tenor.com/NeSd-6B6wl4AAAAC/tu-vas-chialer-spiderman.gif")
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

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

bot.run('MTAxNjMzMTI5ODg3MDE1MzI3Nw.GESou9.g6Mu-i_S-D4R4-1vw5an9Lcs4ovyL_SNNa6Hpg')