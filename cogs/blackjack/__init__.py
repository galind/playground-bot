from core.bot import Playground
from .blackjack import Blackjack


async def setup(bot: Playground):
    await bot.add_cog(Blackjack(bot))
