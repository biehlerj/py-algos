from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """Removes duplicate items from a sorted array

    Parameters
    ----------
    nums : List[int]
        The array to find and remove duplicates from

    Returns
    -------
    int
        The number of duplicates removed
    """
    if len(nums) < 2:
        return len(nums)
    i, j = 1, 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1
