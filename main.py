import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

''' loads the .env file to get token id'''
load_dotenv()
# create bot_id variable which it got from .env file bot variable
bot_id = os.getenv('BOT')
# Gives the prefix for bot as /
bot=commands.Bot(command_prefix="/")

# Prints Bot is ready in console when it is
@bot.event
async def on_ready():
    print("The Bot is Ready")

# the command for when someone writes /ping it send Pong as message in discord
@bot.command(name="ping")
async def ping(ctx): 
	await ctx.send("Pong")
bot.run(bot_id)
