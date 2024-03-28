import discord
import os
from typing import Final
from discord.ext import commands
from discord import Client, Message
from dotenv import load_dotenv
from discord import app_commands
import aiohttp
import asyncio
import json

load_dotenv()

TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


global strings
strings = ["hello","hi","yahallo","yo","yooo","good morning","good night","good afternoon","good evening","bye","goodbye","cya"]

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # Enable message events


bot = commands.Bot(command_prefix='/', intents=intents)

async def first_command(interaction):
    await interaction.response.send_message("Hello!")

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync() #slash tree
        print(f"synced {len(synced)} command(s)")
    #syncing slash commands? something like that
    except Exception as e:
        print(e)

# slash command starts
@bot.tree.command(name = "hello")
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey yo,{interaction.user.mention}")

@bot.tree.command(name="neko")
async def neko(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/neko'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)

@bot.tree.command(name="waifu")
async def waifu(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/waifu'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)

@bot.tree.command(name="shinobu")
async def shinobu(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/shinobu'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)

@bot.tree.command(name="megumin")
async def megumin(interaction: discord.Integration):
    url = 'https://api.waifu.pics/sfw/megumin'
    data = await fetch_json(url)
    url = data['url']
    await interaction.response.send_message(url)

@bot.tree.command(name = "say")
@app_commands.describe(describe = "What should i say?")
async def say(interaction: discord.Integration, describe: str):
    await interaction.response.send_message(f"{interaction.user.mention} said: `{describe}`")


#slash command ends

# Define event for when a message is received
@bot.event
async def on_message(message):
    # Check if the message starts with strings[]
    for string in strings:
        if ((message.content.startswith("?"))): # response in private 
                if message.author != bot.user:
                 await message.author.send(f"{message.content} {message.author.mention}!")
                 break


        elif message.content.lower().startswith(string): #in any channel
            if message.author != bot.user:
                await message.channel.send(f'{string.capitalize()} {message.author.mention}!')
            break
        # Send a response mentioning the user who sent the message
        


# Run the bot with your token
bot.run(TOKEN)