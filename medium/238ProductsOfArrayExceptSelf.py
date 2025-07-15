class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = [1] * len(nums)
        post = [1] * len(nums)
        pre[0] = nums[0]
        post[-1] = nums[-1]
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            j = -i - 1
            pre[i] = pre[i-1] * nums[i]
            post[j] = post[j+1] * nums[j]
        for i in range(len(nums)):
            ans[i] = (pre[i - 1] if i > 0 else 1) * (post[i + 1] if i < len(nums) - 1 else 1)
        return ans
        