import re

from bot.commands.Command import Command
from bot.players.YoutubePlayer import YoutubePlayer

class PauseCommand(Command):
    async def execute(self, message):
        self.client.voiceUser.player.pause()