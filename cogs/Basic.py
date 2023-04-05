import discord
from discord.ext import commands, tasks
import random

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Basic.py is connected to Discord")
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.client.latency * 1000)}ms')
        
    @commands.command(aliases=['8ball', 'eight ball', '8 ball'])
    async def eightball(self, ctx):
        with open("outputs/8ball.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)
            
            await ctx.send(response)
            
async def setup(client):
        await client.add_cog(Basic(client))