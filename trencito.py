from inspect import indentsize
import os
import random
 
import discord
# from discord import Interaction
# from discord.ext import tasks, commands
# from discord.ext.commands import Bot
# from discord.ext.commands import Context

from dotenv import load_dotenv
 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
 
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hola {member.name} putite!!!!11!!!'
    )

@client.event
async def on_message(message):
    holas_aleatorios = [
        'Hola putite!!!!11!!!',
        'messi',
        'Tu nariz contra mis bolas'
    ]
    if message.content.startswith('hola'):
        response = random.choice(holas_aleatorios)
        await message.channel.send(response)
    
    if message.content.startswith('tuki'):
        await message.channel.send(file=discord.File('C:/Users/annyp/OneDrive/Escritorio/cosas/botcito/tuki.jpg'))

client.run(TOKEN)