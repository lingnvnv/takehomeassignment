import pytest


@pytest.mark.parametrize("num_student, treats, starting_chair, expected", [
    (5, 2, 1, 2),
    (5, 2, 2, 3),
    (7, 19, 2, 6),
    (3, 7, 3, 3)
])
def test_student_treats(num_student, treats, starting_chair, expected):
    from student_treats import student_treats
    result = student_treats(num_student, treats, starting_chair)
    assert result == expected
