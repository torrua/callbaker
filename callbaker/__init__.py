"""
This module contains all the necessary functions for
creating callback data strings and parsing it from call's data.
"""
from callbaker.constants import (
    DEFAULT_MARK_VALUE,
    DMV,
    EMS,
    EXTERNAL_MARK_SEPARATOR,
    IMS,
    INTERNAL_MARK_SEPARATOR,
)
from callbaker.functions import callback_from_info, info_from_callback

__all__ = [
    "info_from_callback",
    "callback_from_info",
    "DEFAULT_MARK_VALUE",
    "DMV",
    "EXTERNAL_MARK_SEPARATOR",
    "EMS",
    "INTERNAL_MARK_SEPARATOR",
    "IMS",
]
