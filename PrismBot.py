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
    accepted1=False
    view=ui.View()
    button =ui.Button(label="Accept",style=discord.ButtonStyle.gray,emoji="✔")
    async def accepted(interaction):
        if interaction.user==target_user:
                btn1=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0)
                btn2=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0)
                btn3=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0)
                btn4=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1)
                btn5=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1)
                btn6=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1)
                btn7=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2)
                btn8=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2)
                btn9=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2)
                view.remove_item(button)
                view.add_item(btn1)
                view.add_item(btn2)
                view.add_item(btn3)
                view.add_item(btn4)
                view.add_item(btn5)
                view.add_item(btn6)
                view.add_item(btn7)
                view.add_item(btn8)
                view.add_item(btn9)
                await interaction.response.send_message(view=view)
                

    button.callback=accepted
    view.add_item(button) 
    await interaction.response.send_message(f"{target_user.mention} click button to accept",view=view)

     


bot.run(TOKEN)