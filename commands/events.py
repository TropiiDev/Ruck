import discord
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events Online")

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Your forgetting something")
        if isinstance(error, commands.MissingRole):
            await ctx.send("Mate, you dont have the role to execute this command")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Mateyyy, sorry but you dont have the permissions to execute this command")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry, but I dont recall that being a command. Wanna try again? Use `r!help`")
        if isinstance(error, commands.BotMissingRole):
            await ctx.send("MATE I DONT HAVE THE ROLE FOR THIS")
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send("OK I THOUGHT WE WERE FRIENDS? GUESS NOT! I DONT HAVE THE PERMISSIONS TO EXECUTE THIS COMMAND")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Error 404.. Please tell WepWop#3446 the issue and name of command. Thanks <3")
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("Looks like your missing a role.. Check again")

def setup(bot):
    bot.add_cog(events(bot))