from typing import List


def singleNumber(nums: List[int]) -> int:
    """Finds element that appears only once

    Parameters
    ----------
    nums : List[int]
        The list to search

    Returns
    -------
    int
        The element that only appears once
    """
    unique_number = 0
    for i in nums:
        unique_number ^= i
    return unique_number
