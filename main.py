import discord
import time
import logging
import threading
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

class MyClient(discord.Client):
    voice = None
    #audio = discord.FFmpegPCMAudio(source="test.mp3", executable='ffmpeg/bin/ffmpeg.exe')
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if str(message.author.id) == "822239449849135116":
            await message.channel.send('Shut up nigga!')

    async def disconnect(bot, member):  
        print("start before sleep")
        time.sleep(5)
        print("start after sleep")
        await member.edit(voice_channel=None)
        await bot.voice.disconnect()
        bot.voice = None        
        print("finished in")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if str(member.id) == "822239449849135116":
            if after.channel is not None:
                print("Connected")
                if self.voice is not None:
                    if self.voice.is_connected():
                        await self.voice.move_to(after.channel)
                        self.voice.play(discord.FFmpegPCMAudio("oriStfu.mp3"))  
                else:
                    self.voice = await after.channel.connect()
                    self.voice.play(discord.FFmpegPCMAudio("oriStfu.mp3"))
        
                t1 = threading.Thread(target= self.disconnect(self, member), args=(10,))
                print("before start")
                t1.start()
                t1.join()
                print("after join")

            else:
                print("Disconnected")
                await self.voice.disconnect()
                self.voice = None

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents, command_prefix = "!")
client.run(os.environ['TOKEN'])