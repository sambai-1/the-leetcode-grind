class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return 0
        mid = 2**(n-2)
        if k > mid:
            return 1 - self.kthGrammar(n-1, k-mid)
        else:
            return self.kthGrammar(n-1, k)