class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        prev2 = 0

        ans = 0
        for i in nums:
            ans = max(prev2 + i, prev)
            prev2 = prev
            prev = ans
        return ans