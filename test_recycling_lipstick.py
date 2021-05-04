import pytest


@pytest.mark.parametrize("num_lipstick, num_needed, expected", [
    (5, 2, 9),
    (15, 5, 18),
    (2, 3, 2),
])
def test_getTotalNumberOfLipsticks(num_lipstick, num_needed, expected):
    from recycling_lipstick import recycling_lipstick
    
    result = getTotalNumberOfLipsticks(num_lipstick, num_needed)
    assert result == expected
