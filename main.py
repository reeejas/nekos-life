import discord
from discord.ext import commands, tasks
import aiohttp
from aiohttp import request
intents = discord.Intents().all()
intents.members = True
import os
from unicodedata import name
from wsgiref import headers
from itertools import cycle
import json

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

PREFIX = config["prefix_settings"]["prefix"]
STATUS1 = config["status1"]
STATUS2 = config["status2"]
TOKEN = config["token"]

if config["prefix_settings"]["use_space"] == True:
    prefix = PREFIX + ' '


client = commands.Bot(command_prefix=PREFIX,help_command=None,intents = intents)

status = cycle([STATUS1, STATUS2])

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.", delete_after=5)

@client.event
async def on_ready():
    change_status.start()
    print('Logged in as: {0.user}'.format(client), '\nClient ID =', client.user.id)

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'nsfw_cogs.{extension}')
    client.load_extension(f'sfw_gifs_cogs.{extension}')
    client.load_extension(f'real_animals_cogs.{extension}')
    client.load_extension(f'misc_cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'nsfw_cogs.{extension}')
    client.unload_extension(f'sfw_gifs_cogs.{extension}')
    client.unload_extension(f'real_animals_cogs.{extension}')
    client.unload_extension(f'misc_cogs.{extension}')

for filename in os.listdir('./nsfw_cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'nsfw_cogs.{filename[:-3]}')

for filename in os.listdir('./sfw_gifs_cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'sfw_gifs_cogs.{filename[:-3]}')

for filename in os.listdir('./real_animals_cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'real_animals_cogs.{filename[:-3]}')

for filename in os.listdir('./misc_cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'misc_cogs.{filename[:-3]}')

@client.command()
async def list(ctx):
    em = discord.Embed(title = "**LIST OF ALL COMMANDS**", color = ctx.author.color)
    em.add_field(name="**NSFW**",value="`hololewd`  |  `holonsfw`  |  `erok`  |  `lewdk` \n \n `nsfwneko`  |  `eron`  |  `lewd`  |  `ero` \n \n `feet`  |  `erofeet`  |  `gasm`  |  `solo` \n \n `tits`  |  `yuri`  |  `eroyui`  |  `hentai` \n \n `cum`  |  `bj`  |  `femdom`  |  `trap` \n \n `pussy`  |  `futa`  |  `cumg`  |  `solog` \n \n `spank`  |  `lesbian`  |  `bjg`  |  `pwank` \n \n `pussyg`  |  `hentai`  |  `feetg`  |  `pussylick` \n \n `classic`  |  `boobs`  |  `anal`",inline=False)
    em.add_field(name="**SFW GIFS**",value="`pat`  |  `poke`  |  `hug`  |  `cuddle` \n \n `kiss`  |  `feed`  |  `tickle`  |  `smug`  \n \n `baka`  |  `slap`",inline=False)
    em.add_field(name="**SFW NEKOS**",value="`holo`  |  `fox`  |  `nekogif`  |  `neko`",inline=False)
    em.add_field(name="**MISC**",value="`fact`  |  `name`  |  `eightball`  |  `why`  |  `waifu` ",inline=False)
    em.set_footer(icon_url=ctx.author.avatar_url, text = "Made with https://github.com/Nekos-life")
    await ctx.send(embed = em)

client.run(TOKEN)