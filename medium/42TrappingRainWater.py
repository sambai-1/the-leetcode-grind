class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pre = [0] * len(height)
        post = [0] * len(height)

        maxl = maxr = -1
        for i in range(len(height)):
            j = -i - 1
            maxl = max(maxl, height[i])
            pre[i] = maxl
            maxr = max(maxr, height[j])
            post[j] = maxr

        ans = 0
        for i in range(len(height)):
            ans += min(pre[i], post[i]) - height[i]
        
        return ans