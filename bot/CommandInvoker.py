from bot.commands.DisconnectCommand import DisconnectCommand
from bot.commands.PauseCommand import PauseCommand
from bot.commands.PlayCommand import PlayCommand
from bot.commands.ResumeCommand import ResumeCommand
from bot.commands.ShuffleCommand import ShuffleCommand
from bot.commands.StopCommand import StopCommand

class CommandInvoker:
    def __init__(self, client):
        self.client = client

    async def invoke(self, message):
        symbol = '/'

        if message.content.startswith(symbol + 'play'):
            await PlayCommand(self.client).execute(message)
        elif message.content.startswith(symbol + 'disconnect'):
            await DisconnectCommand(self.client).execute(message)
        elif message.content.startswith(symbol + 'pause'):
            await PauseCommand(self.client).execute(message)
        elif message.content.startswith(symbol + 'resume'):
            await ResumeCommand(self.client).execute(message)
        elif message.content.startswith(symbol + 'stop'):
            await StopCommand(self.client).execute(message)
        elif message.content.startswith(symbol + 'shuffle'):
            await ShuffleCommand(self.client).execute(message)
