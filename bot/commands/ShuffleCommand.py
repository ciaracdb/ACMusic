from bot.commands.Command import Command

class StopCommand(Command):
    async def execute(self, message):
        self.client.voiceUser.player.stop()