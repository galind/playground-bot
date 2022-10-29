import asyncio
from core.bot import Playground


async def run_bot():
    bot = Playground()
    await bot.start()


def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
