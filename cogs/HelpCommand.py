import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand.py is connected to Discord.")
        
    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(title="pryBOT's Help Desk", description="List of commands available for pryBOT", color=discord.Color.random())
        
        help_embed.set_author(name="pryBOT")
        help_embed.add_field(name="Clear", value="Removes specified number of messages.", inline=False)
        help_embed.add_field(name="Mute", value="Mutes member.", inline=False)
        help_embed.add_field(name="Unmute", value="Unmutes member.", inline=False)
        help_embed.add_field(name="Kick", value="Kicks member.", inline=False)
        help_embed.add_field(name="Ban", value="Bans Member.", inline=False)
        help_embed.add_field(name="Unban", value="Unbans Member.", inline=False)
        help_embed.add_field(name="Mute Role", value="Sets mute role for server.", inline=False)
        help_embed.add_field(name="Autorole", value="Sets role to be applied upon joining.", inline=False)
        help_embed.add_field(name="Set Prefix", value="Change the default prefix to a custom one.", inline=False)
        help_embed.add_field(name="8ball", value="Let the Magic 8 Ball decide your fate.", inline=False)
        help_embed.add_field(name="Ping", value="Ping the server to see how quickly the bot responds.", inline=False)
        help_embed.add_field(name="Need more help?", value="[Join the support server!](https://discord.gg/a2GXCDtf)", inline=False)
        help_embed.set_footer(text=f"Requested by <@{ctx.author}>.", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=help_embed)



async def setup(client):
    await client.add_cog(HelpCommand(client))
    
