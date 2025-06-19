from typing import List


def canPartition(nums: List[int]) -> bool:
    result = 0
    for i in nums:
        result += i
    if result % 2 != 0:
        return False
    result = result // 2
    tested = {}
    def dfs(curr, index) :
        if curr == 0:
            tested[(curr, index)] = True
        if curr < 0 or index == len(nums):
            tested[(curr, index)] = False
        if (curr, index) in tested:
            return tested[(curr, index)]
        
        if dfs(curr - nums[index], index + 1):
            return True
        else:
            return dfs(curr, index + 1)
    
    return dfs(result, 0)

nums=[1,2,3,4]
print(canPartition(nums))