import discord
import requests
import time
from discord.ext import tasks, commands
from discord.ext.commands import bot

# client = discord.Client()

# async def send_message(message):
#     channel = client.get_channel('724689655999496214')#add channel ID here
#     await channel.sent(message)

# client.run('NzIzNjY0MjEzODM0NDY1MzAw.XvDMgg.Bg1OdMvlBRAtJOeCfbdCZntnTl4') #add Discord bot ID here

class botClient (discord.Client):
    voice_channel = None
    general_channel = None

    async def get_connection(self):
        if self.voice_channel is None:
            channel = self.get_channel()#add channel ID here
            self.voice_channel = await channel.connect()
        return self.voice_channel

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        print('We are in.')
        await self.get_connection()

    # @commands.command(pass_context=True)
    #     async def play(self, ctx, *, url):
    #         print(url)
    #         server = ctx.message.guild
    #         voice_channel = server.voice_client

    #         async with ctx.typing():
    #             player = await YTDLSource.from_url(url, loop=self.bot.loop)
    #             ctx.voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
    #         await ctx.send('Now playing: {}'.format(player.title))

    async def play_audio(self, file): 
        vc = await self.get_connection()
        print('Playing Audio')
        source = discord.FFmpegPCMAudio(file, executable='D:\\Programs\\ffmpeg\\bin\\ffmpeg.exe')
        vc.play(source, after=lambda e: print('done'))

    async def on_message(self, message):
        if message.author == client.user:
            return

        # if message.content.startswith('$poopie'):
        #     await self.play_audio('poopie.mp3')
        
        # if message.content.startswith('Search Room'):
        #     await self.play_audio('search_room.mp3')
        
        if message.content.startswith('Access'):
            if message.content.endswith('Vault of Glass'):
                await message.channel.send("""Here are a list of the enemies in the Vault: 
-Atheon 
-Gorgon
-Templar""")
            if message.content.endswith('Crota'):
                await message.channel.send("""Here is a list of our files on Crota:
-Crota
-Oryx
-Savathun""")
        elif message.content.endswith('Crota'):
            await message.channel.send('Crota was the son of Oryx.')

client = botClient()
client.run()