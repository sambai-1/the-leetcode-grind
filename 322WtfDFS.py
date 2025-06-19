from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    stored = {0: 0}
    coins.sort(reverse = True)
    def dfs(curr):
        if curr in stored:
            return stored[curr]
        stored[curr] = -1
        for i in coins:
            if (curr - i) >= 0:
                tmp = dfs(curr - i) + 1
                if tmp != 0 and (tmp < stored[curr] or stored[curr] == -1):
                    stored[curr] = tmp
                
        return stored[curr]


    
    return dfs(amount)

coins=[11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
amount=330
print(coinChange(coins, amount))