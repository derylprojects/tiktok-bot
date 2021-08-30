import asyncio
import logging

import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

from bot import bot, dp, handlers  # noqa
from settings import ENVIRONMENT, SENTRY_DSN

sentry_sdk.init(
    dsn=SENTRY_DSN,
    environment=ENVIRONMENT,
    integrations=[AioHttpIntegration()]
)


async def main():
    try:
        logging.info('VEEZ TT BOT STARTED')
        await dp.start_polling()
    finally:
        logging.info('VEEZ TT BOT EXITED')
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
