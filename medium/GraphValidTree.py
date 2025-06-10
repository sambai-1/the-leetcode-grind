from collections import defaultdict
from typing import List


def validTree(n: int, edges: List[List[int]]) -> bool:
        edge = defaultdict(list)
        start = -1
        for i in edges:
            x, y = i
            edge[x].append(y)
            edge[y].append(x)
            start = x
        visited = set()
        loop = False

        def dfs(curr, prev, prev2):
            nonlocal loop
            if curr == prev2:
                return
            if curr in visited:
                loop = True
                return
            
            visited.add(curr)
            for i in edge[curr]:
                dfs(i, curr, prev)

        dfs(start, -1, -1)

        if loop:
            return False
        return len(visited) == n or (not edges and n == 1)
    
n = 5
edges=[[0,1],[0,2],[0,3],[1,4]]
print(validTree(n, edges))