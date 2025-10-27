"""
This module contains all the necessary functions for
creating callback data strings and parsing it from call's data.
"""

from callbaker import EMS, IMS, DMV


def info_from_callback(call_data: str, separators: tuple = (EMS, IMS, DMV)) -> dict:
    """

    :param call_data:
    :param separators:
    :return:
    """

    if not isinstance(call_data, str):
        raise TypeError("call_data should be a str type. You input %s." % type(call_data))

    for sep in separators:
        if not isinstance(sep, str):
            raise TypeError("Separator should be a str type. You input %s." % type(sep))

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
    if not isinstance(info, dict):
        raise TypeError("Info should be a dict type. You input %s." % type(info))

    for sep in separators:
        if not isinstance(sep, str):
            raise TypeError("Separator should be a str type. You input %s." % type(sep))

    _ems, _ims, _ = separators

    callback = "".join(["%s%s%s%s" % (_ems, mark, _ims, value) for mark, value in info.items()])

    if len(callback) > 64:
        raise ValueError("The length of callback_data should not be more that 64 symbols."
                         "Your callback's length is %s symbols." % len(callback))
    return callback
