#!/bin/env python3

__version__ = '0.0.2'
VERSION = __version__

__all__ = (
    'Client',
    'NextFunction',
    'TelegramError',
)
from .client import (
    logger,
    Client,
    NextFunction,
    TelegramError,
)
