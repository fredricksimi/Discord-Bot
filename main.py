import discord
import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count += 1
    
    print("NewDevBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("Hi you gorgeous clown")

bot.run(DISCORD_TOKEN)