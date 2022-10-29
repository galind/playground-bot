import discord
from discord import app_commands
from discord.ext import commands
from core.bot import Playground


class Blackjack(commands.Cog):
    def __init__(self, bot: Playground):
        self.bot = bot
