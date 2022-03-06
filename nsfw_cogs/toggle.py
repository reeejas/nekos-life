import discord
from discord.ext import commands

class togggle(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="toggle", description="Enable and disable commands!")
    @commands.is_owner()
    async def toggle(self, ctx, *, command):
        command = self.client.get_command(command)
        if command is None:
            await ctx.send("I can't find a command with this name!", delete_after=5)

        elif ctx.command == command:
            await ctx.send("You cannot disable this command!", delete_after=5)

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f'I have {ternary} {command.qualified_name} for you!', delete_after=5)

def setup(client):
    client.add_cog(togggle(client))