import os
import discord
import asyncio

from discord import ChannelType

from bot.VoiceUser import VoiceUser
from bot.getPlaylistUrls import getPlaylistUrls


class Invoker:
    def __init__(self, client):
        self.voice = None
        self.client = client

    async def executeCommand(self, message):
        symbol = '/'
        voiceUser = VoiceUser(self.client)

        if(message.content.startswith(symbol+'play')):
            self.voice = await voiceUser.joinCommandAuthorVoiceChannel(message.author)

            urls = getPlaylistUrls('https://www.youtube.com/watch?v=JDglMK9sgIQ&list=PLYgkQ-QH58rqIKAYL7AesKHz3wWqJ35gK&index=1')
            for url in urls:
                player = await self.voice.create_ytdl_player(url)
                player.volume = 0.5
                player.start()
                break
        elif(message.content.startswith(symbol+'disconnect')):
            if(self.client.is_voice_connected(message.server)):
                for voiceClient in self.client.voice_clients:
                    await voiceClient.disconnect()
                    break
