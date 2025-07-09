class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calculate(n):
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n = n // 10
            return ans
        
        ans = []
        while n != 1:
            if n in ans:
                return False
            ans.append(n)
            n = calculate(n)
        return True