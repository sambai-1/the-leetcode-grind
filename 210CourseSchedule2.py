class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        prereqs = defaultdict(list)
        for i in prerequisites:
            x, y = i
            prereqs[x].append(y)
        
        visited = set()
        completed = set()
        ans = []
        self.loop = False

        def dfs(curr):
            if curr in visited:
                self.loop = True
                return
            if curr in completed:
                return

            visited.add(curr)
            for i in prereqs[curr]:
                dfs(i)
            visited.remove(curr)
            completed.add(curr)
            ans.append(curr)
            

        for i in range(numCourses):
            dfs(i)
            
        if self.loop:
            return []
        return ans