class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        row1 = row2 = [0] * amount
        for i in coins:
            for j in range(len(row1)):
                val = j + 1
                tmp = 1
                if val - i < 0:
                    tmp = 0
                elif val - i > 0:
                    tmp = row1[j - i]
                
                row1[j] = row2[j] + tmp

            row2 = row1[:]
        
        return row1[-1]