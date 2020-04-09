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


def info_from_callback(call_data: str, separators: tuple = (EMS, IMS, DMV)) -> dict:
    """

    :param call_data:
    :param separators:
    :return:
    """

    _ems, _ims, _ = separators
    separated_items = call_data.split(_ems)
    parsed_items = [element.split(_ims)
                    for element in separated_items if element]
    result = {k: v for k, v in parsed_items if k and v}

    for mark, value in result.items():
        if value.isdigit():
            result[mark] = int(value)
        _ = [result.update({mark: item}) for item in (False, True, None) if value == str(item)]
    return result


def callback_from_info(info: dict, separators: tuple = (EMS, IMS, DMV)) -> str:
    """

    :param info:
    :param separators:
    :return:
    """
    _ems, _ims, _ = separators
    return "".join(["%s%s%s%s" % (_ems, mark, _ims, value) for mark, value in info.items()])


if __name__ == "__main__":
    pass
