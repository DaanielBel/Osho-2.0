import discord
import time
import asyncio
import logging
import threading
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from discord.ext import commands

load_dotenv()

def discon(bot, member):
    member.edit(voice_channel=None)
    bot.voice.disconnect()
    bot.voice = None


class MyClient(discord.Client):
    voice = None
    target = "318475929221332992"
    
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=885615716915642498))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if str(message.author.id) == self.target:
            await message.channel.send('You stupid nigga!')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if str(member.id) == self.target:
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

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents, command_prefix = "^^")
tree = app_commands.CommandTree(client)
client.run(os.environ['TOKEN'])
