class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        '''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.'''
        n = len(prices)
        if n == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(0, n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
        return max_profit