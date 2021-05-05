def student_treats(num_student: int, num_treats: int, starting_chair: int) -> int:
    '''Find the student who received the last treat by distribute the treat cyclically and sequentially

    There are num_student students sitting around circle and each student number
    sequentially as 1, ,2 ... ,num_student, start from the starting_chair, we
    distribute num_treats treats sequentially. The function help determine the student
    who receives the last treat

    Args:
        num_student (int): a positive integer from 1 to 10**9 indicated students number
        num_treats (int): a positive integer from 1 to 10**9 indicated treats number
        starting_chair (int): a positive number indicated starting chair number

    Returns:
        int : the studnet number who receive the last treat

    Raises:
        ValueError: Raises an exception if staring chair is bigger than num_student
        TypeError: if num_student or num_treats or staring chair is not positive integer
    '''
    if type(num_student) is not int or num_student <= 0\
            or type(num_treats) is not int or num_treats <= 0\
            or type(starting_chair) is not int or starting_chair <= 0:
        raise TypeError("Input must be positive integer")
    if starting_chair > num_student:
        raise ValueError("chair number is out of range")
    if num_treats + starting_chair - 1 < num_student:
        return num_treats + starting_chair - 1
    else:
        new_index = (num_treats + starting_chair - 1) % num_student
        return new_index if new_index != 0 else num_student


if __name__ == '__main__':
    pass
