import discord 
from discord.ext import commands

class Embeds(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Embeds.py is connected to Discord')
        
        
    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="Embed Title", description="Embed Description", color=discord.Color.red())
        
        embed_message.set_author(name=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="field name", value="field value", inline=False)
        embed_message.set_footer(text="Embed Footer", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=embed_message)

async def setup(client):
    await client.add_cog(Embeds(client))