import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

class MyClient(discord.Client):
    voice = None

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if str(message.author.id) == "273745908137459712":
            await message.channel.send('Shut up nigga!')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None and not member.bot:
            print("Connected")
            if self.voice is not None:
                if self.voice.is_connected():
                    await self.voice.move_to(after.channel)
            else:
                self.voice = await after.channel.connect()

        else:
            print("Disconnected")
            await self.voice.disconnect()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents, command_prefix = "!")
client.run(os.environ['TOKEN'])