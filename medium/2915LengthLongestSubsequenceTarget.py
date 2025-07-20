class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        seqs = {}
        for num in nums:
            for _, (key, val) in enumerate(seqs.items()):
                newKey = key + num
                if newKey <= target:
                    seqs[newKey] = max(val + 1, seqs.get(newKey, 0))
            if num <= target:
                seqs[num] = max(1, seqs.get(num, 0))
        return seqs.get(target, -1)