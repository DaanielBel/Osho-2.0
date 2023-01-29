import discord
import time
import asyncio
import logging
import threading
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

voice = [{885615716915642498 : None}]
target = [{885615716915642498 : None}]

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

client = commands.Bot(intents=intents, command_prefix = "$$")

def discon(bot, member):
    member.edit(voice_channel=None)
    bot.voice.disconnect()
    bot.voice = None

@client.event
async def on_ready():
    print(f'Logged on as {client}!')

@client.event
async def on_message(ctx, message):
    if message.author.id == "822239449849135116":
        await message.channel.send('You stupid nigga!')

@client.event
async def on_guild_join(guild):
    voice.append({guild.id : None})
    target.append({guild.id : None})

@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
    if str(member.id) == "822239449849135116":
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


@client.commands()
async def target(ctx, tar : discord.member):
    await print(tar)
    await ctx.channel.send(tar)


async def main():
    client.run(os.environ['TOKEN'])

asyncio.run(main())