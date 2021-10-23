import pytest

from callbaker.functions import callback_from_info


@pytest.mark.parametrize("data", [None, False, 234, "str"])
def test_info_not_a_str(data):
    with pytest.raises(TypeError) as _:
        callback_from_info(info=data)


def test_separators_not_a_str():
    with pytest.raises(TypeError) as _:
        callback_from_info(info={"k": "v", }, separators=("1", "2", 3))


def test_info():
    result = callback_from_info(
        info={"k1": "str", "k2": 2, "k3": None, "k4": False, "k5": (1, 2)})
    assert isinstance(result, str)
    assert result == "&k1=str&k2=2&k3=None&k4=False&k5=(1, 2)"


def test_info_wrong():
    with pytest.raises(ValueError) as _:
        callback_from_info(
            info={"k1": "s" * 60, "k2": 2, "k3": None,
                  "k4": False, "k5": (1, 2)})
