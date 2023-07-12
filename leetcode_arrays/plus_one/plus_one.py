from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """Add 1 to the digits created by the given array

    Parameters
    ----------
    digits : List[int]
        The array representing the number to add 1 to

    Returns
    -------
    List[int]
        The new array of digits
    """
    for i, v in reversed(list(enumerate(digits))):
        if i == 0 and v == 9:
            digits[i] = 0
            digits.insert(0, 1)
            break
        elif v == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break

    return digits
