import discord
from discord.ext import commands

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("About Online")

    @commands.command()
    async def about(self, ctx):
        author = ctx.author
        await author.send(f"Sup {author.name},\n\nMy name is Ruck\n\nI was created by a guy named WepWop!\n\nMy purpose is to do funny things for your you and your friends. All im here to do is to just make you laugh and have a good time on discord!\n\nAny suggestions? Please send them all to WepWop#3446. If you dont want to send any suggestions through DM's, and your in Relaxed. Then you can send suggestions through there!")

def setup(bot):
    bot.add_cog(about(bot))