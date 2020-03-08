import os
import discord
import logging

from discord.ext import commands
from dotenv import load_dotenv
from typing import Final

CHANNEL_NAME : Final = "gravy-rpg"

bot = commands.Bot(command_prefix='>')
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class Client(discord.Client):
    async def on_ready(self):
        for guild in client.guilds:
            if guild.id == GUILD:
                break
        print(guild.name)

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Hi {member.name}, welcome to this discord server, feel free to try out the RPG game running in the `gravy-rpg` channel'
        )

    async def on_message(self, message):
        if message.content.find(">hello") != -1:
            await message.channel.send("Welcome stranger")

if __name__=="__main__":
    load_dotenv()

    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    GUILD = os.getenv('DISCORD_SERVER_NAME')

    client = Client()
    client.run(TOKEN)
