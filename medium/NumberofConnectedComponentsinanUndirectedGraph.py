from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union = [-1] * n
        def parent(curr):
            if union[curr] == -1:
                return curr
            return parent(union[curr])

        for x, y in edges:
            x = parent(x)
            y = parent(y)
            if x != y:
                union[min(x, y)] = max(x, y)

        counter = 0
        for i in union:
            if i == -1:
                counter +=1
        return counter