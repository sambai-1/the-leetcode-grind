class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        def search(nums):
            a = 0
            b = 0

            ans = 0
            for i in nums:
                ans = max(i + a, b)
                a = b
                b = ans
            return ans
        
        return max(search(nums[1:]), search(nums[:-1]))