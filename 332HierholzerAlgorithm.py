from collections import defaultdict
from typing import List


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        paths = defaultdict(list)
        for x, y in tickets:
            paths[x].append(y)
        for x in paths.keys():
            paths[x].sort()
        print(paths)
        
        ans = []
        visited = []
        def dfs(curr):
            visited.append(curr)
            if not paths[curr]:
                if any(paths.values()):
                    visited.pop() #IMPORTANT TO DO POP NOT REMOVE(CURR) cuz otherwise removes first instance
                    return False
                ans.extend(visited)
                return True
            
            for i in range(len(paths[curr])):
                next = paths[curr].pop(i)
                if dfs(next):
                    return True
                paths[curr].insert(i, next)
            
            visited.pop()
            return False
        
        dfs("JFK")

        return ans

#Wow better solution is actually incredible
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        paths = defaultdict(list)
        for x, y in tickets:
            paths[x].append(y)
        for x in paths.keys():
            paths[x].sort(reverse = True)
        print(paths)
        
        ans = []
        todo = ["JFK"]
        while todo:
            while paths[todo[-1]]:
                todo.append(paths[todo[-1]].pop())
            ans.append(todo.pop())
        return ans[::-1]

tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
print(findItinerary(tickets))