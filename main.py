import asyncio
import random
import discord
import requests
import youtube_dl
import aiml
import pkg_resources
import os

from discord.ext import commands
from fox import info
from 대답 import response


client = commands.Bot(command_prefix='!')

async def func_comeon(ctx):
    voice = voice_client_in(ctx.message.server)
    if ctx.message.author.voice.voice_channel:
        if voice:
            if voice.channel != ctx.message.author.voice.voice_channel:
                print('move to channel')
                await voice.move_to(ctx.message.author.voice.voice_channel)
        else:
            print('join to channel')
            voice = await join_voice_channel(ctx.message.author.voice.voice_channel)
    else:
        await say('where are you?')
        print('stay...')
    return voice
 
@client.command(pass_context=True)
async def comeon(ctx):
    await func_comeon(ctx)
 
@client.command(pass_context=True)
async def play(ctx):
    voice = await func_comeon(ctx)
    player = voice.create_ffmpeg_player('바젤.mp3')
    player.start()






client.run(info.TOKEN)
