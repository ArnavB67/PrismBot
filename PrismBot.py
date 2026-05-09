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
turnx=0
turny=0
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
    player1=interaction.user
    player2=target_user
    accepted1=False
    view=ui.View()
    button =ui.Button(label="Accept",style=discord.ButtonStyle.gray,emoji="✔")
    async def accepted(interaction):
        if interaction.user==target_user:
                btn1=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0,custom_id='0')
                btn2=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0,custom_id='1')
                btn3=ui.Button(label="O",style=discord.ButtonStyle.gray,row=0,custom_id='2')
                btn4=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1,custom_id='3')
                btn5=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1,custom_id='4')
                btn6=ui.Button(label="O",style=discord.ButtonStyle.gray,row=1,custom_id='5')
                btn7=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2,custom_id='6')
                btn8=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2,custom_id='7')
                btn9=ui.Button(label="O",style=discord.ButtonStyle.gray,row=2,custom_id='8')
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
                buttons=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]

                async def play(interaction):
                    global turnx
                    global turny
                    index=int(interaction.data["custom_id"])
                    clicked_button=buttons[index]
                    if interaction.user==player1 and turnx==turny:
                         clicked_button.style=discord.ButtonStyle.red
                         clicked_button.label="X"
                         turnx+=1
                         await interaction.response.edit_message(view=view)
                    elif interaction.user==player2 and turnx>turny:
                            clicked_button.style=discord.ButtonStyle.blurple
                            clicked_button.label="O"
                            turny+=1
                            await interaction.response.edit_message(view=view)
                btn1.callback=play
                btn2.callback=play
                btn3.callback=play
                btn4.callback=play
                btn5.callback=play
                btn6.callback=play
                btn7.callback=play
                btn8.callback=play
                btn9.callback=play


    button.callback=accepted
    view.add_item(button) 
    await interaction.response.send_message(f"{target_user.mention} click button to accept",view=view)

     


bot.run(TOKEN)