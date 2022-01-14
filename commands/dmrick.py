import discord
from discord.ext import commands

class dmrick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DMRick Online")

    @commands.command()
    async def dmrick(self, ctx, member:discord.Member):
        await member.send(f"Sup {member.name},\n\nSo I just found this funny meme right,\n\n Click this link to see it..\n\n https://r.mtdv.me/discordVQ")

def setup(bot):
    bot.add_cog(dmrick(bot))