from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) + 1)
        memo[-1] = 0
        nums.append(float("inf"))
        for i in range(len(nums) - 2, -1, -1):
            most = -1
            for j in range(i + 1, len(nums)):
                if memo[j] >= most and nums[j] > nums[i]:
                    most = memo[j]
            memo[i] = most + 1
        
        ans = 0
        for i in memo:
            ans = max(ans, i)
        return ans