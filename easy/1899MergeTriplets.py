class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        ans = [-1, -1, -1]
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                ans[0] = max(ans[0], a)
                ans[1] = max(ans[1], b)
                ans[2] = max(ans[2], c)
        
        return True if ans == target else False