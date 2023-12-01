from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@dataclass
class TelegramBot:
    bot_token: str

@dataclass
class Config:
    telegram_bot: TelegramBot


def load_config() -> Config:
    return Config(
        telegram_bot=TelegramBot(
            bot_token=getenv('BOT_TOKEN')
        )
    )

__all__ = (
    'load_config',
)