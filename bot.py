import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
import json

def get_server_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    return prefix[str(message.guild.id)]

client = commands.Bot(command_prefix = get_server_prefix, intents=discord.Intents.all())

bot_status = cycle(['[REDACTED]', '[ERROR]'])

@client.event
async def on_ready():
    await client.tree.sync()
    print('\npryBOT connected successfully\n')
    change_status.start()
    
@client.tree.command(name="ping", description="test")
async def pingg(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"{bot_latency}ms")
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the required permissions to run this command.")
    
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(guild.id)] = ">"
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
    
    with open("cogs/outputs/mute.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
    
    with open("cogs/outputs/mute.json", "w") as f:
        json.dump(mute_role, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix.pop(str(guild.id))
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
    
    with open("cogs/outputs/mute.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role.pop[str(guild.id)] = None
    
    with open("cogs/outputs/mute.json", "w") as f:
        json.dump(mute_role, f, indent=4)

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))
    
@client.command()
async def setprefix(ctx, *, newprefix: str):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(ctx.guild.id)] = newprefix
    
    with open("prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)
    
        
        

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")
    print("\nAll cogs loaded successfully\n")

async def main():
    async with client:
        await load()
        await client.start("MTA3NDM5MjA1NzQ5MTIyNjYyNA.Gv_xOl.QFMaUuk1qpeLPcSewjw6Og4gR4VCBO_Eo3AZr4")


asyncio.run(main())

