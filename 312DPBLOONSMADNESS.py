class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0] * (len(nums) + 2) for _ in range(len(nums) + 2)]
        for i in range(len(nums) + 2):
            dp[0][i] = dp[i][len(nums) + 1] = 1
        
        nums = [1] + nums[:] + [1]
        
        for i in range(len(nums) - 2, -1, -1):
            for j in range(0, i):
                x = j + 1
                y = j + (len(nums) - i - 2) + 1
                ans = -1
                for k in range(x, y + 1):
                    curr = nums[x - 1] * nums[k] * nums[y + 1]
                    curr = curr + dp[x][k - 1] + dp[k + 1][y]
                    ans = max(ans, curr)
                dp[x][y] = ans

        return dp[1][len(nums) - 2]
    
#try dfs approach next