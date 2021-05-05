import pytest
from least_factorial import least_factorial


class TestAssert():
    @pytest.mark.parametrize("n, expected", [
        (17, 24),
        (5, 6),
        (106, 120)
    ])
    def test_least_factorial(self, n, expected):
        result = least_factorial(n)
        assert result == expected

    def test_exception_match(self):
        with pytest.raises(ValueError) as excinfo:
            least_factorial(0)
        assert excinfo.type == ValueError
        assert 'input should be a postive integer from 1 to 120' in str(
            excinfo.value)
