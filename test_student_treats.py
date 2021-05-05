import pytest
from student_treats import student_treats
class TestAssert():

    @pytest.mark.parametrize("num_student, treats, starting_chair, expected", [
        (5, 2, 1, 2),
        (5, 2, 2, 3),
        (7, 19, 2, 6),
        (3, 7, 3, 3)
    ])
    def test_student_treats(self, num_student, treats, starting_chair, expected):
        result = student_treats(num_student, treats, starting_chair)
        assert result == expected

    def test_exception_match(self):
        with pytest.raises(TypeError) as excinfo:
            student_treats(-1, -2, 0.2)
        assert excinfo.type == TypeError
        assert "Input must be positive integer" in str(
            excinfo.value)
        with pytest.raises(ValueError) as excinfo:
            student_treats(5, 3, 6)
        assert excinfo.type == ValueError
        assert "hair number is out of range" in str(
            excinfo.value
