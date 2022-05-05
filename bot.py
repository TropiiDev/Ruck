import discord
from discord.ext import commands
from discord_slash import SlashCommand
import help
from commands import dmrick, events, bozo, hehe, wave, about, frank, invite, suggest
from ext.eventext import whatresponse
from dotenv import load_dotenv
import os
from asyncio import sleep

load_dotenv('.env')

cogs = [dmrick, events, help, bozo, hehe, wave, about, frank, invite, suggest, ]

bot = commands.AutoShardedBot(commands.when_mentioned_or("r!"), intents = discord.Intents.all())
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)

for i in range(len(cogs)):
    cogs[i].setup(bot)

@bot.event
async def on_ready():
    print("Bot Online")

@bot.command()
async def test(ctx, *, commands=None):
    if commands == help:
        exec(open('help.py').read())

# slash ping command
@slash.slash(description="Sends the bots latency!")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# slash help command
@slash.slash(description="Sends the bots help!")
async def help(ctx):
    em = discord.Embed(title="Help", description="Here is the list of commands you can use!", color=ctx.author.color)
    em.add_field(name="r!help|/help", value="Sends the bots help!", inline=False)
    em.add_field(name="r!ping|/ping", value="Sends the bots latency!", inline=False)
    em.add_field(name="r!dmrick|/dmrick", value="Sends a message to a user!", inline=False)
    em.add_field(name="r!bozo|/bozo", value="Sends a bozo message!", inline=False)
    em.add_field(name="r!hehe|/hehe", value="Sends a hehe message!", inline=False)
    em.add_field(name="r!wave|/wave", value="Sends a wave message!", inline=False)
    em.add_field(name="r!about|/about", value="Sends the bots about!", inline=False)
    em.add_field(name="r!frank|/frank", value="Sends a frank message!", inline=False)
    em.add_field(name="r!invite|/invite", value="Sends the bots invite link!", inline=False)
    em.add_field(name="r!suggest|/suggest", value="Sends the bots invite link!", inline=False)
    await ctx.send(embed=em)

@slash.slash(description="Sends a about the bot message to the message author")
async def about(ctx):
    em = discord.Embed(title="About", description="This is a bot made by <@!293934384559098880>", color=ctx.author.color)
    em.add_field(name="Github", value="https://github.com/WepWop/Ruck.git")
    em.add_field(name="Discord", value="https://discord.gg/Y3wfceRb77")
    em.add_field(name="Support", value="https://discord.gg/Y3wfceRb77")
    em.add_field(name="Invite", value="https://discord.gg/Y3wfceRb77")
    em.add_field(name="Website", value="To soon be built!")
    em.add_field(name="Version", value="1.0.0")
    em.add_field(name="Author", value="Tropiiツ#3446")
    em.add_field(name="Thanks", value="Tropiiツ#3446 for making this bot!")
    em.add_field(name="About", value="This bot was made by Tropiiツ#3446 for the purpose of having fun with discord!")
    await ctx.send(embed=em)

@slash.slash(description="I cannot expose this secret command!")
async def dmrick(ctx, *, member: discord.Member):
     await member.send(f"Sup {member.name},\n\nSo I just found this funny meme right,\n\n Click this link to see it..\n\n https://r.mtdv.me/discordVQ")

@slash.slash(description="Tells the mentioned member that they are a bozo")
async def bozo(ctx, *, member: discord.Member):
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

@slash.slash(description="Tells the mentioned member to eat a frank")
async def frank(ctx, *, member: discord.Member):
    guild = ctx.guild
    await member.send(f"{ctx.author.mention} in {guild} wants you to eat a ")
    await member.send("f")
    await member.send("r")
    await member.send("a")
    await member.send("n")
    await member.send("k")
    await member.send("Lol, have a nice day!")
    await ctx.send("Done!")

@slash.slash(description="The mentioned member gets hehed")
async def hehe(ctx, *, member: discord.Member):
    author = ctx.author
    hehe = 'http://images5.fanpop.com/image/polls/850000/850347_1318054584356_full.jpg'

    em = discord.Embed(title="You have just been hehe'd! LOL...", description="", color = author.color)
    em.set_image(url=hehe)

    await member.send(embed=em),

@slash.slash(description="Want to invite the mentioned member to the server?")
async def invite(ctx, *, member: discord.Member):
    await member.send(f"{ctx.author.mention} wants you to join the Relaxed server!\n\n https://discord.gg/Y3wfceRb77")

@slash.slash(description="Suggest something to the bot owner!")
async def suggest(ctx, *, suggestion):
    author = ctx.author
    await bot.get_user(875604204889202698).send(f"{author.name} has suggested {suggestion}")
    await ctx.send(f"Thanks for your suggestion {author.name}! It has been sent to <@875604204889202698>")

@slash.slash(description="Sends a wave message to the mentioned member")
async def wave(ctx, *, member: discord.Member):
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

bot.run(os.getenv("TOKEN"))