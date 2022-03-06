import discord
from discord.ext import commands
from aiohttp import request

class eerok(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def erok(self, ctx):
        URL = "https://nekos.life/api/v2/img/erok"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data["url"])

            else:
                await ctx.send(f"API returned a {response.status} status.")

def setup(client):
    client.add_cog(eerok(client))