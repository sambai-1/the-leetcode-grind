class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [{} for i in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for k, v in dp[i].items():
                dp[i + 1][k + nums[i]] = dp[i + 1].get(k + nums[i], 0) + v
                dp[i + 1][k - nums[i]] = dp[i + 1].get(k - nums[i], 0) + v
        
        return dp[-1].get(target, 0)