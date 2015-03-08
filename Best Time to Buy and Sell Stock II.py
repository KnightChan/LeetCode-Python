class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        '''Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).'''
        n = len(prices)
        if n <= 1:
            return 0
        l = 0
        r = 0
        sum = 0
        up = False
        while r + 1 < n:
            if up:
                if prices[r + 1] >= prices[r]:
                    r += 1
                else:
                    sum += prices[r] - prices[l]
                    l = r
                    r += 1
                    up = not up
            else:
                if prices[r] >= prices[r + 1]:
                    r += 1
                else:
                    l = r
                    r += 1
                    up = not up
        if up:
            sum += prices[r] - prices[l]
        return sum

a1 = [2, 1]
a2 = [1, 2, 4, 5, 2, 3, 1]
a = a2
print(a)
print(Solution.maxProfit(Solution(), a))