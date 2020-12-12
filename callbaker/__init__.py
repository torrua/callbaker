# -*- coding: utf-8 -*-
"""
This module contains all the necessary functions for
creating callback data strings and parsing it from call's data.
"""

EXTERNAL_MARK_SEPARATOR = "&"
INTERNAL_MARK_SEPARATOR = "="
DEFAULT_MARK_VALUE = "*"

EMS = EXTERNAL_MARK_SEPARATOR
IMS = INTERNAL_MARK_SEPARATOR
DMV = DEFAULT_MARK_VALUE

from callbaker.functions import info_from_callback, callback_from_info
