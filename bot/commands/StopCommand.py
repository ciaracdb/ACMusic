from bot.commands.Command import Command

class PauseCommand(Command):
    async def execute(self, message):
        self.client.voiceUser.player.pause()