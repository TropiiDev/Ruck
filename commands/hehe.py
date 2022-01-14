import discord
from discord.ext import commands

class hehe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("HeHe Online")

    @commands.command()
    async def hehe(self, ctx, member:discord.Member):
        author = ctx.author
        hehe = 'http://images5.fanpop.com/image/polls/850000/850347_1318054584356_full.jpg'

        em = discord.Embed(title="You have just been hehe'd! LOL...", description="", color = author.color)
        em.set_image(url=hehe)

        await member.send(embed=em),

def setup(bot):
    bot.add_cog(hehe(bot))