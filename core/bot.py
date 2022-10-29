import discord
from discord.ext import commands
from . import config

initial_extensions = (
    'cogs.blackjack',
    'cogs.owner',
)


class Playground(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
        )


    async def setup_hook(self):
        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Loaded: {extension}')
            except Exception as e:
                print(f'Not loaded: {extension}\n{e}')


    async def on_ready(self):
        print(f'Ready: {self.user}')


    async def start(self):
        return await super().start(
            config.APPLICATION_TOKEN,
            reconnect=True
        )
