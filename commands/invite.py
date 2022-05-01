import discord
from discord.ext import commands

class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Invite Online")

    @commands.command()
    async def invite(self, ctx):
        em = discord.Embed(title="Invite Links", description="", color = ctx.author.color)
        em.add_field(name="Bot Invite:", value="https://discord.com/api/oauth2/authorize?client_id=920440364991655957&permissions=8&scope=bot%20applications.commands")
        em.add_field(name="Support Server:", value="https://discord.gg/Y3wfceRb77")

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(invite(bot))