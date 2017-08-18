import os
import discord
import logging

from bot.DiscordClient import DiscordClient

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

if __name__ == '__main__':
    if not discord.opus.is_loaded():
        discord.opus.load_opus('/tmp/opus-build/opus_sm-master/libopus.so')

    client = DiscordClient()
    client.run(os.environ.get('BOT_TOKEN'))