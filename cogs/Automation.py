import discord
from discord.ext import commands
import json

class Automation(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Automation.py is connected to Discord.")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        with open("json/autorole.json", "r") as f:
            auto_role = json.load(f)
        
        join_role = discord.utils.get(member.guild.roles, name=auto_role[str(member.guild.id)])
        
        await member.add_roles(join_role)
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def joinrole(self, ctx, role: discord.Role):
        with open("json/autorole.json", "r") as f:
            auto_role = json.load(f)
            
        auto_role[str(ctx.guild.id)] = str(role.name)
        
        with open("json/autorole.json", "w") as f:
            json.dump(auto_role, f, indent=4)
            
        conf_embed = discord.Embed(color=discord.Color.green())
        conf_embed.add_field(name="Success!", value=f"Successfully set the join role to {role.name}.")
        conf_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=conf_embed)
        
async def setup(client):
    await client.add_cog(Automation(client))