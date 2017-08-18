from bot.commands.Command import Command

class ResumeCommand(Command):
    async def execute(self, message):
        self.client.voiceUser.player.resume()