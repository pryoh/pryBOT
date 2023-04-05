import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio
import json

client = commands.Bot(command_prefix = '=', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("pryBOT is connected to Discord")
    
    
@client.command()
async def ping (ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

client.run("MTA3NDM5MjA1NzQ5MTIyNjYyNA.GNKTsn.4oyRAxhgVQDODTu2VypxYz-MeGjPAbImeF_HVI")


