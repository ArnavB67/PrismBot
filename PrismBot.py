import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from discord import ui
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")
intents=discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is ready")


@bot.tree.command(name="hello",description="greets the bot")
async def hello(interaction:discord.Interaction):

    username=interaction.user.mention
    await interaction.response.send_message(f"hello there, {username}")

@bot.tree.command(name="tictactoe",description="play tic tac toe")
async def tictactoe(interaction:discord.Interaction,target_user:discord.Member):
    view=ui.View()
    button =ui.Button(label="Accept",style=discord.ButtonStyle.gray,emoji="✔")
    async def accepted(interaction):
        if interaction.user==target_user:
                await interaction.response.send_message(f"challeng accepted by {target_user.mention}")
                accepted=True
    button.callback=accepted
    view.add_item(button)

    
    await interaction.response.send_message(f"{target_user.mention} click button to accept",view=view)




bot.run(TOKEN)