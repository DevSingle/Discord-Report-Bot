import asyncio
import os
from nextcord import Intents
import nextcord
from nextcord.ext.commands import Bot
from nextcord.ext import commands
from nextcord.ext.commands.errors import CommandNotFound
bot = Bot(command_prefix="Bot Prefix", intents=Intents().all(), help_command=None, case_insensitive=True) #set You Bot Prefix = !

loaded_extensions = {}
for path, subdirs, files in os.walk('cogs/'):
    for name in files:
        if name.endswith('.py'):
            filename = os.path.join(path, name).replace('/', '.').replace('\\', '.')[:-3]
            cog_name = name[:-3].split('.')[-1]       
            loaded_extensions[cog_name] = filename
            bot.load_extension(filename)
bot.loaded_extensions = loaded_extensions
async def status_task(): #Status Task
    while True:
        await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="❤ Red Moon Server")) #Status Text And Type
        await asyncio.sleep(60)
        guild = bot.get_guild(GULD ID) #GUILD ID = server id
        await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=f'🔰 {len(guild.members)} Members!')) #Status Text And Type
        await asyncio.sleep(60)

@bot.event
async def on_ready():
    print(f"""
    Bot Runned!
""")
    bot.loop.create_task(status_task()) # Run Status Task

        
bot.run("BOT TOKEN") #You Bot Token