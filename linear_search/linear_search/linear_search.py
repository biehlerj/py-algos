def linear_search(arr: list[int], arr_len: int, target: int) -> int:
    """Finds the target value in an array of arr_len

    Parameters
    ----------
    arr : list[int]
        The array to search
    arr_len : int
        The length of the array
    target : int
        The number to find in the array

    Returns
    -------
    int
        A number representing the index of the target
    """
    for i in range(0, arr_len):
        if arr[i] == target:
            return i
    return -1
