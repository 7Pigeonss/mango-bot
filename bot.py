import os
import logging
import discord

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

if not TOKEN:
	raise RuntimeError("Missing DISCORD_BOT_TOKEN environment variable")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print(f"🥭 Mango Bot online as {client.user}")


@client.event
async def on_message(message):
	if client.user and message.author.id == client.user.id:
		return

	try:
		await message.add_reaction("🥭")
	except discord.HTTPException as error:
		logging.warning("Could not react: %s", error)


client.run(TOKEN)
