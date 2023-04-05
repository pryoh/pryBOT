import discord 
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation is ready')
        
        
        

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"Purged {count} messages.")
        
        
        
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(member, reason=reason)
        
        # Create an embed to show that the member was kicked
        embed = discord.Embed(title="Member Kicked", color=0xff0000)
        embed.add_field(name="User", value=member.mention, inline=False)
        embed.add_field(name="Kicked by", value=ctx.author.mention, inline=False)
        if reason:
            embed.add_field(name="Reason", value=reason, inline=False)
            
        # Send a message to the kicked member
        try:
            await member.send(f"You were kicked from {ctx.guild.name} by {ctx.author.mention}")
        except discord.Forbidden:
            pass


        await ctx.send(embed=embed)
        
        
        
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(member)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Banned:", value=f"{member.mention}", inline=False)
        conf_embed.add_field(name="Banned by:", value=f"{ctx.author.mention}", inline=False)
        if reason:
            conf_embed.add_field(name="Reason:", value=reason, inline=False)
            
        # Send a message to the kicked member
        try:
            await member.send(f"You were banned from {ctx.guild.name} by {ctx.author.mention}")
        except discord.Forbidden:
            pass

        
        await ctx.send(embed=conf_embed)
        
        
        
        
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unbanned:", value=f"<@{userId}> has been unbanned from the server by {ctx.author.mention}.", inline=False)
            
        await ctx.send(embed=conf_embed)
            
            
            
            
async def setup(client):
    await client.add_cog(Moderation(client))