from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top = 1
        for i in matrix[0]:
            if i == 0:
                top = 0
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        print(matrix)
        if top == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        return 
        