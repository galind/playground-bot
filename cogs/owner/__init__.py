from core.bot import Playground
from .owner import Owner


async def setup(bot: Playground):
    await bot.add_cog(Owner(bot))
