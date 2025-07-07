class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        l = t = 0
        r = len(matrix[0])
        b = len(matrix)
        x = y = 0
        while l < r and t < b:
            for i in range(l, r):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                ans.append(matrix[i][r - 1])
            
            r -= 1
            if not (l < r and t < b):
                return ans

            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1

        return ans