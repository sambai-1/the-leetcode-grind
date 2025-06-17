class Solution:
    def climbStairs(self, n: int) -> int:
        ans = {1: 1, 2: 2}
        def fib(curr):
            if curr in ans:
                return ans[curr]
            ans[curr] = fib(curr - 1) + fib(curr - 2)
            return ans[curr]

        fib(n)
        return ans[n]
        