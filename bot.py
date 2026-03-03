import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")  # Get token from environment variable

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.CustomActivity(
            name="🚀 Running On Best!"
        )
    )

bot.run(TOKEN)
