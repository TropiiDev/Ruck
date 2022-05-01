import discord
from discord.ext import commands

class frank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Frank Online")

    @commands.command()
    async def frank(self, ctx, member:discord.Member):
        guild = ctx.guild
        await member.send(f"{ctx.author.mention} in {guild} wants you to eat a ")
        await member.send("f")
        await member.send("r")
        await member.send("a")
        await member.send("n")
        await member.send("k")
        await member.send("Lol, have a nice day!")
        await ctx.send("Done!")

def setup(bot):
    bot.add_cog(frank(bot))