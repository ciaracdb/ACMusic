import re

from bot.commands.Command import Command
from bot.players.YoutubePlayer import YoutubePlayer
from bot.utils.getPlaylistUrls import getPlaylistUrls

class PlayCommand(Command):
    async def execute(self, message):
        channelIsJoined = await self.client.voiceUser.joinCommandAuthorVoiceChannel(message.author)

        if not channelIsJoined:
            return

        p = re.compile('/play (.+)')
        url = p.match(message.content).group(1)

        if 'youtube' in url:
            self.client.voiceUser.player = YoutubePlayer(self.client)
        else:
            self.client.voiceUser.player = YoutubePlayer(self.client)

        if 'list=' in url:
            urls = getPlaylistUrls(url)
            for itemUrl in urls:
                self.client.voiceUser.player.addToQueue(itemUrl)
        else:
            self.client.voiceUser.player.addToQueue(url)

        await self.client.voiceUser.player.startQueue()