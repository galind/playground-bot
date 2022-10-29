from core.bot import Economy
from .owner import Owner


async def setup(bot: Economy):
    await bot.add_cog(Owner(bot))
