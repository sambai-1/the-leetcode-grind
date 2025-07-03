class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        ans = 0
        while r < (len(nums)):
            nextR = r
            while l < r:
                nextR = max(l + nums[l], nextR)
                l += 1
            r = nextR + 1
            ans += 1

        return ans