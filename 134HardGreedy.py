class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        completed = 0
        for i in range(len(gas)):
            gas[i] -= cost[i]
            completed += gas[i]

        if completed < 0:
            return -1
        
        ans = 0
        current = 0
        for i in range(len(gas)):
            current += gas[i]
            if current < 1:
                current = 0
                ans = i + 1
        
        return ans % len(gas)