import discord
import logging
import asyncio
from botKey import Key
from dict import DictionaryHandler

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("------------")


@client.event
async def on_message(message):
	r = DictionaryHandler()

client.run(Key()._get_value())