import pytest


@pytest.mark.parametrize("n, expected", [
    (17, 24),
    (5, 6),
    (106, 120)
])
def test_least_factorial(n, expected):
    from least_factorial import least_factorial
    
    result = least_factorial(n)
    assert result == expected


