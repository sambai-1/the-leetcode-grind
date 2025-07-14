class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        ans = []
        
        for i in range(len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            ans.extend([[nums[i]] + curr for curr in self.permute(tmp)])

        return ans
