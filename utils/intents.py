import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True