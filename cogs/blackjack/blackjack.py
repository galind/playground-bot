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
    return shuffle_deck(deck)


def shuffle_deck(deck: list):
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def calculate_hand(hand: list):
    aces = [c for c in hand if c[0] == 'A']
    non_aces = [c for c in hand if c[0] != 'A']

    hand_sum = 0
    for c in non_aces:
        hand_sum += cards[c[0]]
    for c in aces:
        if hand_sum <= 10:
            hand_sum += 11
        else:
            hand_sum += 1
    return hand_sum


class GameButtons(discord.ui.View):
    def __init__(self, bot: Playground):
        self.bot = bot
        super().__init__(timeout=None)


class Blackjack(commands.Cog):
    def __init__(self, bot: Playground):
        self.bot = bot


    @app_commands.command(name='blackjack')
    async def blackjack_command(self, interaction: discord.Interaction):
        """Start a blackjack game"""
        pass
