import discord
from discord.ext import commands
from aiohttp import request

class leewd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lewd(self, ctx):
        URL = "https://nekos.life/api/v2/img/lewd"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

            else:
                await ctx.send(f"API returned a {response.status} status.")

def setup(client):
    client.add_cog(leewd(client))