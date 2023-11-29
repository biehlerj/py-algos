from typing import List


def moveZeroes(nums: List[int]) -> None:
    """Moves all zeroes in the list to the end in-place

    Parameters
    ----------
    nums : List[int]
        The list to move zeroes in

    """
    if len(nums) == 1:
        return
    try:
        found = nums.index(0)
        zeros_count = 1
    except ValueError:
        return

    while found is not None:
        nums.pop(found)
        try:
            found = nums.index(0)
            zeros_count += 1
        except ValueError:
            found = None

    while zeros_count != 0:
        nums.append(0)
        zeros_count -= 1
