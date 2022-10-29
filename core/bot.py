import discord
from discord.ext import commands
from . import config

initial_extensions = ()


class Playground(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        for extension in initial_extensions:
            try:
                pass
            except:
                pass

    async def on_ready(self):
        print(f'Ready: {self.user}')

    async def start(self):
        return await super().start(
            config.APPLICATION_TOKEN,
            reconnect=True
        )
