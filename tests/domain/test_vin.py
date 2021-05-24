import pytest

from fictional.domain.fields import to_friendly_vin


@pytest.mark.current
@pytest.mark.parametrize("param", (
        (None, 1, "1", "1" * 16, "3" * 18, "a" * 17,)
))
def test_invalid_vin(param):
    with pytest.raises(TypeError):
        to_friendly_vin(param)


@pytest.mark.parametrize("param, expected", (
        (48123658489411439, "481-23658-8-9-41-1439"),
        ("48123658489411439", "481-23658-8-9-41-1439"),
))
def test_valid_vin(param, expected):
    assert to_friendly_vin(param) == expected
