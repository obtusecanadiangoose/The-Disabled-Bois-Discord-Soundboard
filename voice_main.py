import asyncio

import discord

from discord.ext import commands


token = 'DISCORD_TOKEN'

ffmpeg_options = {
    'options': '-vn'
}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def any8(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/8yo.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def hehe(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/ahehehe.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def areu(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/areuabababa.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def bomb(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/BOMB YOU RETARD.wav"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @commands.command()
    async def calmdown(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/canhecalmdown.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def plant(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/canuplant.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def eatshit(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/eatshit.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def how(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/hooow.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def five(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/howmanyis5.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def huhu(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/huhuhuhuwhat.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def v1(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/ifulosethis1v1.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def howtf(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/ohohohohowhatthefuck.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def scream(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/screamofanguish.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def shoothim(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/SHOOT HIM.wav"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def shesdead(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/siebrenshesdead.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def turnedon(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/turnedon.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def insane(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/uractuallyinsane.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
 
    @commands.command()
    async def surprise(self, ctx):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/wahahaha.mp3"))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
      
    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @any8.before_invoke
    @hehe.before_invoke
    @areu.before_invoke
    @bomb.before_invoke
    @calmdown.before_invoke
    @plant.before_invoke
    @eatshit.before_invoke
    @how.before_invoke
    @five.before_invoke
    @huhu.before_invoke
    @v1.before_invoke
    @howtf.before_invoke
    @scream.before_invoke
    @shoothim.before_invoke
    @shesdead.before_invoke
    @turnedon.before_invoke
    @insane.before_invoke
    @surprise.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("*"),
                   description='Relatively simple music bot example')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(Music(bot))
bot.run(token)
