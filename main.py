import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if str(message.author.id) == "273745908137459712":
            await message.channel.send('Shut up nigga!')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if type(after.channel) != "NoneType" and not member.bot:
            print(member.name + " joined " + after.channel.name)
            client = await client.join_voice_channel(after.channel.id)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents, command_prefix = "!")
client.run(os.environ['TOKEN'])