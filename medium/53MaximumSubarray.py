class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -100001
        current = 0
        for i in nums:
            if current < 0:
                current = 0
            current += i
            ans = max(ans, current)
        
        return ans
        