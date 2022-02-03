"""Utils module."""
import asyncio
import logging
import random
import string
from datetime import datetime
from uuid import uuid4

from aiogram.types import Message


async def shallow_sleep_async(sleep_time: float = 0.1) -> None:
    await asyncio.sleep(sleep_time)


def gen_uuid() -> str:
    return uuid4().hex


def gen_random_str(length=4) -> str:
    return ''.join(
        random.SystemRandom().choice(string.ascii_lowercase + string.digits) for
        _
        in range(length))


def format_ts(ts: float, time_format: str = '%a %b %d %H:%M:%S %Y') -> str:
    return datetime.fromtimestamp(ts).strftime(time_format)


def bold(text: str) -> str:
    """Wrap input string in HTML bold tag."""
    return f'<b>{text}</b>'


def code(text: str) -> str:
    """Wrap input string in HTML code tag."""
    return f'<code>{text}</code>'


def get_user_info(message: Message) -> str:
    """Return user information who interacts with bot."""
    chat = message.chat
    return f'Request from user_id: {chat.id}, username: {chat.username}, ' \
           f'full name: {chat.full_name}'


def build_command_presentation(commands: dict[str, list]) -> str:
    groups = []
    for desc, cmds in commands.items():
        groups.append(
            '{0}\n{1}'.format(desc, '\n'.join(['/' + c for c in cmds])))
    return '\n\n'.join(groups)


def setup_logging(suppress_asyncio: bool = True,
                  suppress_urllib3: bool = True) -> None:
    log_format = '%(asctime)s - [%(levelname)s] - [%(name)s:%(lineno)s] - %(message)s'
    logging.basicConfig(format=log_format)
    if suppress_asyncio:
        logging.getLogger('asyncio').setLevel(logging.WARNING)

    if suppress_urllib3:
        logging.getLogger('urllib3').setLevel(logging.WARNING)
