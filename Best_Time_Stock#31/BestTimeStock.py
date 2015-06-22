# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
        	return 0
        low, high, maxProfit = -1, -1, 0
        if prices[0] >= prices[1]:
        	low = prices[1]
        else:
        	low = prices[0]
        	high = prices[1]
        	maxProfit = high - low
        prePrice = prices[1]
        for idx,price in enumerate(prices[1:]):
        	if high == -1:
        		if price <= low:
        			low = price
        		else:
        			high = price
        			maxProfit = max(maxProfit,high-low)
        		continue
        	if price < low:
        		low = price
        		high = -1
        	if price >= high:
        		high = price
        		maxProfit = max(maxProfit,high-low)
        return maxProfit
