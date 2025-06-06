class Solution(object):
    def subsets(self, nums):
        
        ans = []
        curr = []
        def dfs(nums):
            if not nums:
                ans.append(curr[:])
                return

            dfs(nums[1:])
            curr.append(nums[0])
            dfs(nums[1:])
            curr.pop()

        dfs(nums)

        return ans