class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        look = set(nums)
        ans = 0
        for i in look:
            if (i - 1) not in look:
                tmp = 1
                current = i
                while (current + 1) in look:
                    current = current + 1
                    tmp += 1
                ans = max(ans, tmp)
        return ans