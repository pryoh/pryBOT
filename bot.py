import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import json

client = commands.Bot(command_prefix = '=', intents=discord.Intents.all()) #command to set bot prefix

@client.event ##### command to check if bot is connected to Discord
async def on_ready():
    print("pryBOT is connected to Discord")
    change_status.start()
    
    

bot_status = cycle(['[REDACTED]', '[ERROR]'])

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))
    
        
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
        

async def main():
    async with client:
        await load()
        await client.start("MTA3NDM5MjA1NzQ5MTIyNjYyNA.Gv_xOl.QFMaUuk1qpeLPcSewjw6Og4gR4VCBO_Eo3AZr4")


asyncio.run(main())

