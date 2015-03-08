class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        '''Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).'''
        n = len(prices)
        if n <= 1:
            return 0
        min_price = prices[0]
        ltor_profits = [0] * n
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            ltor_profits[i] = max(ltor_profits[i - 1], prices[i] - min_price)

        rtol_profits = [0] * (n + 1)
        rtol_profits[n] = 0
        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            rtol_profits[i] = max(rtol_profits[i + 1], max_price - prices[i])
        max_profit = 0
        for i in range(0, n):
            max_profit = max(max_profit, ltor_profits[i] + rtol_profits[i + 1])
        return max_profit

a1 = [2, 1]
a2 =  	[3,2,6,5,0,3]
a = a2
print(a)
print(Solution.maxProfit(Solution(), a))