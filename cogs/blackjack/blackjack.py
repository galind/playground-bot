import random
import discord
from discord import app_commands
from discord.ext import commands
from core.bot import Playground

cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

suits = [
    '♠️',
    '♦️',
    '♣️',
    '♥️'
]


def get_deck():
    deck = []
    for s in suits:
        for c in cards:
            deck.append(f'{c}{s}')
    return deck


def suffle_deck(deck):
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


class Blackjack(commands.Cog):
    def __init__(self, bot: Playground):
        self.bot = bot


    @app_commands.command(name='blackjack')
    async def blackjack_command(self, interaction: discord.Interaction):
        """Start a blackjack game"""
        pass
