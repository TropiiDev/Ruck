import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Online")

    @commands.command()
    async def help(self, ctx):
        author = ctx.author
        em = discord.Embed(title="Help", description="", color = author.color)
        em.add_field(name="DMRick", value="Try it on your friends..")
        em.add_field(name="Bozo", value="Calls one someone you mention a bozo")
        em.add_field(name="HeHe", value="Hehe one of your friends from the iconic michael jackson")
        em.add_field(name="Wave", value="Sends a bunch of waves to someone")
        em.add_field(name="About", value="About the bot!")
        await author.send(embed=em)

def setup(bot):
    bot.add_cog(help(bot))