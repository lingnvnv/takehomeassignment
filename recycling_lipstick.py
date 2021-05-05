def getTotalNumberOfLipsticks(num_lipstick: int, left_needed: int) -> int:
    '''calculate the total number of lipsticks by setting intial finished
    lipsticks number and recycling lipsticks leftover

    There are ‘num_lipstick‘ in your possession, assuming each of customers
    return their lipsticks leftover, with left_needed (number of Leftovers
    Needed) lipsticks left, owner can make a new lipstick. By cyclically made
    new lipsticks with left over returned by customer, we can calculate the
    total number of lipsticks we sell in total.

    Args:
        num_lipstick (int): the initial number of finished lipsticks in possesion
        left_need: the number of lipstick leftover we need to make a new lipstick

    Returns:
        int : the number of lipstick we can sell  in total
    Raises:
        ValueError: Raises an exception if num_lipstick or left_needed is not a
        positive integer
    '''
    if type(num_lipstick) is not int or type(left_needed) is not int\
            or num_lipstick <= 0 or left_needed <= 0:
        raise ValueError(
            "number of lipsticks and number of lipsticks needed to make a new one have to be integer")
    total = num_lipstick
    left = num_lipstick
    while left >= left_needed:
        total += left // left_needed
        left = left % left_needed + left // left_needed
    return total


if __name__ == "__main__":
    pass
