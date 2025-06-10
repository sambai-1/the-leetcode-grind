class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereqs = defaultdict(list)
        for i in prerequisites:
            x, y = i
            prereqs[x].append(y)
        
        visited = set()
        completed = set()
        def dfs(curr):
            if curr in completed:
                return True
            if curr in visited:
                return False
            if curr not in prereqs:
                return True
            visited.add(curr)
            for i in prereqs[curr]:
                if not dfs(i):
                    return False
            visited.remove(curr)
            completed.add(curr)
            return True

        for i, j in prereqs.items():
            if not dfs(i):
                return False
        return True