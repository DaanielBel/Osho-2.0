import discord
import time
import logging
import threading
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

def waitForThis():
    print("now the time has passed")

class MyClient(discord.Client):
    voice = None
    #audio = discord.FFmpegPCMAudio(source="test.mp3", executable='ffmpeg/bin/ffmpeg.exe')
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if str(message.author.id) == "822239449849135116":
            await message.channel.send('Shut up nigga!')      

    async def dis(self, member):
        time.sleep(5)
        await member.edit(voice_channel=None)
        await self.voice.disconnect()
        self.voice = None

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
                
                t1 = threading.Thread(self.voice.play(discord.FFmpegPCMAudio("oriStfu.mp3")))
                t2 = threading.Thread(self.dis(member))
                
                t1.start()
                t2.start()

                t1.join()
                t2.join()

            else:
                print("Disconnected")
                await self.voice.disconnect()
                self.voice = None

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents, command_prefix = "!")
client.run(os.environ['TOKEN'])