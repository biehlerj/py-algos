from typing import List


def rotate(nums: List[int], k: int) -> None:
    """Rotates an array to the right by k steps in-place

    Parameters
    ----------
    nums : List[int]
        The array to rotate
    k : int
        The amount of times to rotate the array
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
