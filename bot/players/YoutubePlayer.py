import asyncio

from bot.players.Player import Player

class YoutubePlayer(Player):

    def __init__(self, client):
        super().__init__(client)
        self.discordPlayer = None

    async def startQueue(self):
        await self.next()

    def songFinished(self):
        coroutine = self.next()
        future = asyncio.run_coroutine_threadsafe(coroutine, self.client.loop)
        try:
            future.result()
        except:
            pass

    async def next(self):
        if not self.queue.empty():
            self.discordPlayer = await self.client.voiceUser.voiceClient.create_ytdl_player(self.queue.get(), after=self.songFinished)
            self.discordPlayer.volume = 0.5
            self.discordPlayer.start()

    def pause(self):
        self.discordPlayer.pause()

    def resume(self):
        self.discordPlayer.resume()

    def stop(self):
        self.discordPlayer.stop()
