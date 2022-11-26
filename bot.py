import discord
from discord.ext import commands
import help
from commands import dmrick, events, bozo, hehe, wave, about, frank, invite, suggest
from ext.eventext import whatresponse
from dotenv import load_dotenv
import os
from asyncio import sleep

load_dotenv('.env')

cogs = [dmrick, events, help, bozo, hehe, wave, about, frank, invite, suggest, ]

bot = commands.AutoShardedBot(commands.when_mentioned_or("r!"), intents = discord.Intents.all())
bot.remove_command("help")

for i in range(len(cogs)):
    cogs[i].setup(bot)

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(os.getenv("TOKEN"))
