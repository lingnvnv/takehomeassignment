def least_factorial(n: int) -> int:
    '''Find the smallest factorial which is not less than n

    Given an integer n (1 ≤ n ≤ 120), the function find the
    minimal k such that k = m! (where m! =1*2*... *m) for
    some integer m, where k≥n

    Args:
        n (int): a positive integer from 1 to 120

    Returns:
        int : the smallest factorial integer which is not less
        than n

    Raises:
        ValueError: Raises an exception if input is not a positive
        integer from 1 to 120
    '''
    if type(n) is not int or n < 1 or n > 120:
        raise ValueError("input should be a postive integer from 1 to 120")
    m, product = 1, 1
    while product < n:
        m += 1
        product *= m
    return product


if __name__ == "__main__":
    pass
