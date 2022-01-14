import discord
from discord.ext import commands
from asyncio import sleep

class bozo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Bozo Online")

	@commands.command()
	async def bozo(self, ctx, member:discord.Member):
		author = ctx.author
		await member.send(f"Sup {member.name},\n\n The author of this message aka {author.name}, \n\n thinks your a ...")
		await sleep(3)
		await member.send("b")
		await sleep(3)
		await member.send("o")
		await sleep(3)
		await member.send("z")
		await sleep(3)
		await member.send("o")
		await sleep(3)
		await member.send("Lol, thanks for letting me waste your time")
		await ctx.send("Sent LOL")

def setup(bot):
	bot.add_cog(bozo(bot))