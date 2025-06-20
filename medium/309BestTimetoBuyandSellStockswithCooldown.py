def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dp = {}
    def dfs(i, buy):
        if i >= len(prices):
            return 0
        if (i, buy) in dp:
            return dp[(i, buy)]
        
        if buy:
            buying = -prices[i] + dfs(i + 1, False)
            waiting = dfs(i + 1, True)
            dp[(i, buy)] = max(buying, waiting)
        else:
            selling = prices[i] + dfs(i + 2, True)
            waiting = dfs(i + 1, False)
            dp[(i, buy)] = max(selling, waiting)
        return dp[(i, buy)]

    return dfs(0, True)

print(maxProfit([3,2,6,5,0,3]))