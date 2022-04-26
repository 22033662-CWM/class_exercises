import pytest
from UselessCal import UselessCal

@pytest.mark.parametrize(
    "test_input",
    [(2, 3, 4, 5, 6, 7), (1.1, 2, 3, 3.3)]
)
def test_UselessCalAdd_float_int(test_input):
    uc = UselessCal()
    actual = uc.add(*test_input)
    expected = sum(test_input)
    assert actual == expected
