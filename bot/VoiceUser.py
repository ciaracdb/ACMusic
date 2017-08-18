import os
import discord
import asyncio

from discord import ChannelType

class VoiceUser:

    def __init__(self, client):
        self.client = client
        self.voiceClient = None
        self.player = None

    async def joinCommandAuthorVoiceChannel(self, author):
        for channel in self.client.get_all_channels():
            if channel.type == ChannelType.voice and author in channel.voice_members:
                self.voiceClient = await self.client.join_voice_channel(channel)
                return True

        # if author not in a voice channel
        for channel in self.client.get_all_channels():
            if channel.type == ChannelType.voice and len(channel.voice_members):
                self.voiceClient = await self.client.join_voice_channel(channel)
                return True

        return False