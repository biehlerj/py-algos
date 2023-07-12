from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """Checks a list for duplicate items

    Parameters
    ----------
    nums : List [int]
        List to search

    Returns
    -------
    bool
        True if contains duplicates otherwise False
    """
    dup_dict = dict.fromkeys(nums)
    for i in range(len(nums)):
        if dup_dict[nums[i]] is None:
            dup_dict[nums[i]] = 1
        else:
            dup_dict[nums[i]] += 1
    if max(dup_dict.values()) > 1:
        return True
    return False
