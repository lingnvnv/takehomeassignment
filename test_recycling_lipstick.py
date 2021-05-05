import pytest
from recycling_lipstick import getTotalNumberOfLipsticks


class TestAssert():
    @pytest.mark.parametrize("num_lipstick, left_needed, expected", [
        (5, 2, 9),
        (15, 5, 18),
        (2, 3, 2)
    ])
    def test_getTotalNumberOfLipsticks(self, num_lipstick, left_needed, expected):
        result = getTotalNumberOfLipsticks(num_lipstick, left_needed)
        assert result == expected

    def test_exception_match(self):
        with pytest.raises(ValueError) as excinfo:
            getTotalNumberOfLipsticks(0.5, 0.2)
        assert excinfo.type == ValueError
        assert 'number of lipsticks and number of lipsticks needed to make a new one have to be integer' in str(
            excinfo.value)
