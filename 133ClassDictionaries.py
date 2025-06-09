
from collections import deque


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = {}
        
        visited[node] = Node(node.val)
        todo = deque([node])
        while todo:
            curr = todo.popleft()
            for i in curr.neighbors:
                if i not in visited:
                    todo.append(i)
                    visited[i] = Node(i.val)
                tmp = visited[i]
                visited[curr].neighbors.append(tmp)
        
        return visited[node]