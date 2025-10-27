# 👨‍🍳 callbaker

[![Download Callbaker](https://img.shields.io/pypi/v/callbaker.svg)](https://pypi.python.org/pypi/callbaker)
[![codecov](https://codecov.io/gh/torrua/callbaker/branch/master/graph/badge.svg?token=CHCS5JEGZI)](https://codecov.io/gh/torrua/callbaker)

Конвертер callback-запросов для Telegram

## Описание

Этот небольшой пакет помогает парсить данные callback-запросов для телеграм-ботов.

## Установка

``pip install callbaker``

## Использование

Две основные функции, которые могут быть полезны:
- `info_from_callback` преобразует строку callback-данных в словарь
- `callback_from_info` объединяет словарь в строку для callback-запросов

Примеры:

```
result = callback_from_info(info={"k1": "str", "k2": 2, "k3": None, "k4": False, "k5": (1, 2)})
print(result)
```
```"&k1=str&k2=2&k3=None&k4=False&k5=(1, 2)"```


```
result = info_from_callback(call_data="&key_1=value_1&key_2=value_2")
print(result)
```
```{'key_1': 'value_1', 'key_2': 'value_2'}```
