import discord
from discord.ext import commands
from commands import dmrick, events, help, bozo, hehe, wave, about
import os
from dotenv import load_dotenv

load_dotenv(".env")

cogs = [dmrick, events, help, bozo, hehe, wave, about]

bot = commands.AutoShardedBot(commands.when_mentioned_or("r!"), intents = discord.Intents.all())
bot.remove_command("help")

for i in range(len(cogs)):
    cogs[i].setup(bot)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command()
async def test(ctx):
    await ctx.send("Test Complete!")

bot.run(os.getenv("TOKEN"))
