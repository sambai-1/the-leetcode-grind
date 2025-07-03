class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps = 0
        curr = 0
        while jumps >= 0:
            if nums[curr] > jumps:
                jumps = nums[curr]
            jumps -= 1
            curr += 1
            if (curr == len(nums)):
                return True
        
        return curr == len(nums)