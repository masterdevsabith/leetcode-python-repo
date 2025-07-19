# url : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

#### QUESTION####
# You are given an integer array prices where prices[i] is the price of a given stock
# on the ith day.

# On each day, you may decide to buy and / or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.


# SOLUTION#
class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > profit:
                profit = prices[i]-min_price

        return profit


sol = Solution()
result = sol.maxProfit([7, 1, 5, 3, 6, 4])
result2 = sol.maxProfit([1, 2, 3, 4, 5])
result3 = sol.maxProfit([7, 6, 4, 3, 1])
print(f'result of first array : {result}')
print(f'result of second array : {result2}')
print(f'result of third array : {result3}')
