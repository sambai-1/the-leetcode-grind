class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        numbers = {}
        if (len(hand) % groupSize != 0):
            return False

        for i in hand:
            numbers[i] = 1 + numbers.get(i, 0)
        
        sortNumber = [list(kv) for kv in sorted(numbers.items())]

        for j in range(len(hand) // groupSize):
            toRemove = []
            prev = sortNumber[0][0] - 1
            for i in range(groupSize):
                if i >= len(sortNumber):
                    return False
                if sortNumber[i][0] != prev + 1:
                    return False
                sortNumber[i][1] -= 1
                prev = sortNumber[i][0]
                if sortNumber[i][1] == 0:
                    toRemove.append(i)
            for i in range(len(toRemove) - 1, -1, -1):
                sortNumber.pop(toRemove[i])
        
        return True