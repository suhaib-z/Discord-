import os
import discord

# ---------------------------------------------------
# OWO EVENT MANAGER - simple command-reply bot
# Add your commands in the COMMANDS dictionary below.
# Format:  "word you type": "what the bot replies",
# ---------------------------------------------------
COMMANDS = {
    "&start": "🏁 Ready to race? 🏎️💨🔥",
    "&info": (
        "🎯 **HuntBot Event** 🎯\n"
        "Get ready, hunters! The HuntBot event is starting now, "
        "and everyone gets an equal shot at winning. 🏹\n\n"
        "📜 **Rules**\n"
        "• Claim hb in the given channel to take part\n"
        "• Only claims made in the given channel will be counted\n"
        "• The event runs till month end\n"
        "• The player with the best hb wins\n"
        "• If any 2 players score the same, the prize will be "
        "distributed equally between them\n\n"
        "⚖️ **Fair Play**\n"
        "• Everyone has the same rules and the same time period\n"
        "• No cheating, spamming, or using multiple accounts\n"
        "• Staff decisions are final\n\n"
        "Good luck, and may the best hunter win! 🔥"
    ),
    # Add new commands below, one per line:
    # "&word": "reply text",
}

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # also enable this in the Developer Portal

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(
        activity=discord.Game(name="Owo Event Manager")
    )


@client.event
async def on_message(message):
    if message.author.bot:
        return

    text = message.content.strip().lower()
    reply = COMMANDS.get(text)
    if reply:
        await message.channel.send(reply)


if not TOKEN:
    raise SystemExit("DISCORD_TOKEN environment variable is not set.")

client.run(TOKEN)
