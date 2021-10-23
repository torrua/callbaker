import pytest

from callbaker.functions import info_from_callback


@pytest.mark.parametrize("data", ["key_1=value_1", "&key_1=value_1"])
def test_call_data_1(data):
    result = info_from_callback(call_data=data)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert result == {'key_1': 'value_1'}


def test_call_data_2():
    result = info_from_callback(
        call_data="&key_1=value_1&key_2=value_2")
    assert isinstance(result, dict)
    assert len(result) == 2
    assert result == {'key_1': 'value_1', 'key_2': 'value_2'}


@pytest.mark.parametrize("data", [None, False, 234])
def test_call_data_not_a_str(data):
    with pytest.raises(TypeError) as _:
        info_from_callback(call_data=data)


def test_separators_not_a_str():
    with pytest.raises(TypeError) as _:
        info_from_callback(call_data="test", separators=("1", "2", 3))


def test_call_data_without_separators():
    with pytest.raises(ValueError) as _:
        info_from_callback(call_data="test")


@pytest.mark.parametrize("value", (None, False, True))
def test_call_data_bool(value):
    result = info_from_callback(
        call_data="&key_1=%s" % value)
    assert isinstance(result, dict)
    assert result['key_1'] == value


def test_call_data_digit():
    result = info_from_callback(
        call_data="&key_1=20")
    assert isinstance(result, dict)
    assert result['key_1'] == 20


def test_call_data_skip_item():
    result = info_from_callback(
        call_data="&key_10=1&key_2=&key_3=30")
    assert isinstance(result, dict)
    assert len(result) == 2
