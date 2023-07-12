from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """Finds the intersection of two arrays

    Parameters
    ----------
    nums1 : List[int]
        First array to search
    nums2 : List[int]
        Second array to search

    Returns
    -------
    List[int]
        The array of the intersection

    """
    nums_dict = {}
    res = []

    for i in nums1:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1

    for j in nums2:
        if j in nums_dict:
            if nums_dict[j] > 1:
                nums_dict[j] -= 1
            else:
                del nums_dict[j]

            res.append(j)

    return res
