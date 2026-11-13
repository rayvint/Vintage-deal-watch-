import os
import discord

TOKEN = os.environ.get("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Vintage Deal Watch is online as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("Vintage Deal Watch is alive!")

if TOKEN:
    client.run(TOKEN)
else:
    print("Missing DISCORD_TOKEN")
