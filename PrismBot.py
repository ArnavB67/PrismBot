import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")

intents=discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")



bot.run(TOKEN)