from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    if nums[0] + nums[-1] == target:
        return [0, len(nums) - 1]
    for i in range(len(nums)):
        try:
            if nums.index(target - nums[i]) != i:
                return [i, nums.index(target - nums[i])]
        except ValueError:
            pass