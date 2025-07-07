class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix[0]) - 1 - i):
                tmp = matrix[i][j]
                x, y = i, j
                for k in range(3):
                    newx, newy = len(matrix) - y - 1, x
                    matrix[x][y] = matrix[newx][newy]
                    x, y = newx, newy
                matrix[x][y] = tmp
        
        return