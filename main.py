import discord
import time
import asyncio
import logging
import threading
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
client = commands.Bot(intents=intents, command_prefix = "$")

def discon(bot, member):
    member.edit(voice_channel=None)
    bot.voice.disconnect()
    bot.voice = None

voice = None
target = [{885615716915642498 : 318475929221332992}]

@client.event
async def on_ready(self):
    print(f'Logged on as {self.user}!')

@client.event
async def on_message(self, message):
    if str(message.author.id) == self.target:
        await message.channel.send('You stupid nigga!')

@client.command()
async def target(self, tar: discord.member):
    print("target")
    self.target = str(tar.id)


@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
    if member.id == target(member.guild.id):
        if after.channel is not None:
            print("Connected")
            if self.voice is not None:
                if self.voice.is_connected():
                    await self.voice.move_to(after.channel)     
            else:
                self.voice = await after.channel.connect()

            self.voice.play(discord.FFmpegPCMAudio("youStupid.mp3"))
            await asyncio.sleep(1.5)
            await member.edit(voice_channel=None)
            await self.voice.disconnect()
            self.voice = None
        else:
            print("Disconnected")
            await self.voice.disconnect()
            self.voice = None

async def main():
    await client.start(os.environ['TOKEN'])

asyncio.run(main())