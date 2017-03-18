import discord
import logging
import asyncio
from discord import HTTPException
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
	dic = DictionaryHandler()
	if message.author == client.user:
		return
	if message.content.startswith('!'):
		await messageHandler(message)

@client.event
async def on_member_join(member):
	await sendWelcomeMessage(member)


async def sendWelcomeMessage(member):
	dic = DictionaryHandler()
	msg = dic.commandHandler('welcome')
	await client.send_message(member, msg)

async def messageHandler(message):
	await basicMessage(message)

async def basicMessage(message):
	dic = DictionaryHandler()

	try:
		roles = len(message.author.roles)
	except Exception:
		roles = 10

	command = message.content[1::].split(' ')[0].lower()
	msg = dic.commandHandler(message.content[1::], message.channel.name)
	if msg != None:
		if 'help' not in message.content:
			await client.send_message(message.channel, msg)
		else:
			await client.send_message(message.author, msg)
			try:
				await client.delete_message(message)
			except(HTTPException, Forbidden):
				print("message delete error")
	else:
		msg = dic.commandHandler('invalid', message.channel.name)
		await client.send_message(message.author, msg)
		try:
			await client.delete_message(message)
		except (HTTPException, Forbidden):
			print('message delete error')



client.run(Key()._get_value())