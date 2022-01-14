import discord
from discord.ext import commands
from asyncio import sleep

class wave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Wave Online")
    
    @commands.command()
    async def wave(self, ctx, member:discord.Member):
        author = ctx.author

        await member.send(f"You just got waved..")
        await sleep(5)
        await member.send("You wonder why nothing happened")
        await sleep(10)
        await member.send("Especially in a bot thats meant to troll everyone..")
        await sleep(15)
        await member.send("Wait...")
        await sleep(20)
        await member.send("Did the person who just sent this get trolled...")
        await sleep(25)
        await member.send("HAHA")
        await author.send("I couldn't troll this one im sorry.. :sob: please dont hurt me")

def setup(bot):
    bot.add_cog(wave(bot))