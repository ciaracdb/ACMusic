from bot.commands.Command import Command
from bot.utils.getPlaylistUrls import getPlaylistUrls

class DisconnectCommand(Command):
    async def execute(self, message):
        if self.client.is_voice_connected(message.server):
            for voiceClient in self.client.voice_clients:
                await voiceClient.disconnect()
                break
