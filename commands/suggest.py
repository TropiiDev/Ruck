import discord
from discord.ext import commands

# create a cog
class suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Suggest Ready")

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        await ctx.send(f"Your suggestion has been sent to the bot owner. Thank you for your input!")
        await self.bot.get_user(self.bot.owner_id).send(f"Suggestion from {ctx.author.name}: {suggestion}")

# setup the cog
def setup(bot):
    bot.add_cog(suggest(bot))