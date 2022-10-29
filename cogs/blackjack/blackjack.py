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
    'Spades',
    'Diamonds',
    'Clubs',
    'Hearts'
]


def shuffle_deck(deck: list):
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def get_deck():
    deck = []
    for s in suits:
        for c in cards:
            deck.append(f'{c} of {s}')
    return shuffle_deck(deck)


def random_number(deck_len: int):
    return random.randint(0, deck_len - 1)


def calculate_hand(hand: list):
    aces = [c for c in hand if c[0] == 'A']
    non_aces = [c for c in hand if c[0] != 'A']

    hand_sum = 0
    for c in non_aces:
        hand_sum += cards[c.split()[0]]
    for c in aces:
        if hand_sum <= 10:
            hand_sum += 11
        else:
            hand_sum += 1
    return hand_sum


def game_table(dealer_hand, player_hand):
    embed = discord.Embed(title='Blackjack Game')

    dealer_sum = calculate_hand(dealer_hand)
    embed.add_field(
        name='Dealer Hand',
        value='\n'.join(dealer_hand) + f'\n__Value: {dealer_sum}__',
        inline=False
    )

    player_sum = calculate_hand(player_hand)
    embed.add_field(
        name='Player Hand',
        value='\n'.join(player_hand) + f'\n__Value: {player_sum}__',
        inline=False
    )
    return embed


class GameButtons(discord.ui.View):
    def __init__(self, bot: Playground, deck: list, dealer_hand: list, player_hand: list):
        self.bot = bot
        self.deck = deck
        self.dealer_hand = dealer_hand
        self.player_hand = player_hand
        super().__init__(timeout=None)


    @discord.ui.button(label='Hit', custom_id='blackjack:hit', style=discord.ButtonStyle.primary)
    async def hit_button(self, interaction: discord.Interaction, button: discord.Button):
        pass


    @discord.ui.button(label='Stay', custom_id='blackjack:stay', style=discord.ButtonStyle.primary)
    async def stay_button(self, interaction: discord.Interaction, button: discord.Button):
        pass


class Blackjack(commands.Cog):
    def __init__(self, bot: Playground):
        self.bot = bot


    @app_commands.command(name='blackjack')
    async def blackjack_command(self, interaction: discord.Interaction):
        """Start a blackjack game"""
        deck = get_deck()

        player_hand = []
        card = deck.pop(random_number(len(deck)))
        player_hand.append(card)

        dealer_hand = []
        card = deck.pop(random_number(len(deck)))
        dealer_hand.append(card)

        card = deck.pop(random_number(len(deck)))
        player_hand.append(card)

        embed = game_table(dealer_hand, player_hand)
        view = GameButtons(self.bot, deck, dealer_hand, player_hand)
        await interaction.response.send_message(embed=embed, view=view)
