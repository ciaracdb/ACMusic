import discord

from bot.CommandInvoker import CommandInvoker
from bot.VoiceUser import VoiceUser


class DiscordClient(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

        self.commandInvoker = CommandInvoker(self)
        self.voiceUser = VoiceUser(self)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.content.startswith('/'):
            await self.commandInvoker.invoke(message)