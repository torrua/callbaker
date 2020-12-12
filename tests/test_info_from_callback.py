import pytest

from callbaker import info_from_callback


class TestInfoFromCallback:
    """

    """

    bool_tuple = (None, False, True)

    @pytest.mark.parametrize("data", ["key_1=value_1", "&key_1=value_1"])
    def test_call_data_1(self, data):
        result = info_from_callback(call_data=data)
        assert isinstance(result, dict)
        assert len(result) == 1
        assert result == {'key_1': 'value_1'}

    def test_call_data_2(self):
        result = info_from_callback(
            call_data="&key_1=value_1&key_2=value_2")
        assert isinstance(result, dict)
        assert len(result) == 2
        assert result == {'key_1': 'value_1', 'key_2': 'value_2'}

    @pytest.mark.parametrize("data", [None, False, 234])
    def test_call_data_not_a_str(self, data):
        with pytest.raises(TypeError) as _:
            info_from_callback(call_data=data)

    def test_separators_not_a_str(self):
        with pytest.raises(TypeError) as _:
            info_from_callback(call_data="test", separators=("1", "2", 3))

    def test_call_data_without_separators(self):
        with pytest.raises(ValueError) as _:
            info_from_callback(call_data="test")

    @pytest.mark.parametrize("value", bool_tuple)
    def test_call_data_bool(self, value):
        result = info_from_callback(
            call_data="&key_1=%s" % value)
        assert isinstance(result, dict)
        assert result['key_1'] == value

    def test_call_data_digit(self):
        result = info_from_callback(
            call_data="&key_1=20")
        assert isinstance(result, dict)
        assert result['key_1'] == 20
