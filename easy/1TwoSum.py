def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    prev = {}

    for i in range(len(nums)):
        curr = nums[i]
        if (target - curr) in prev:
            return [i, prev[target - curr]]
        prev[curr] = i