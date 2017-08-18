from bot.commands.Command import Command

class ShuffleCommand(Command):
    async def execute(self, message):
        self.client.voiceUser.player.shuffle()