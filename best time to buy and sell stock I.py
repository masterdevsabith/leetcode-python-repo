# class Solution(object):
#     def maxProfit(self, prices):

#         minimum_price = min(prices)
#         maximum_price = max(prices)
#         buy_stock = 0
#         sell_stock = 0
#         profit = 0

#         for smallest_price in prices:
#             if smallest_price == minimum_price:
#                 buy_stock += smallest_price
#                 for biggest_price in prices:
#                     if biggest_price == maximum_price and (prices.index(biggest_price) > prices.index(buy_stock)):
#                         sell_stock += biggest_price
#                         print(
#                             f'index of maximum price : {prices.index(biggest_price)}')
#                         print(
#                             f'index of minimum price : {prices.index(smallest_price)}')
#                         print(sell_stock)
#                         print(biggest_price)
#         profit += sell_stock - buy_stock
#         print(f'minimum price : {minimum_price}')
#         print(f'maximum price : {maximum_price}')
#         print(f'buy : {buy_stock}')
#         print(f'sell : {sell_stock}')
#         return profit


# if prices.index(buy_stock) > prices.index(sell_stock):
#  return profit
#  elif prices.index(buy_stock) < prices.index(sell_stock):
#     profit += sell_stock-buy_stock
#   return profit


### NEW CODE###
# class Solution(object):
#     def maxProfit(self, prices):

#         minimum_price = min(prices)
#         maximum_price = max(prices)
#         buy_stock = 0
#         sell_stock = 0
#         profit = 0

#         for biggest_price in prices:
#             for smallest_price in prices:
#                 if (prices.index(smallest_price) < prices.index(biggest_price)) and ((smallest_price >= minimum_price) and (biggest_price <= maximum_price)):
#                     print(f'smallest_price : {smallest_price}')
#                     print(f'biggest_price : {biggest_price}')
#                     buy_stock += smallest_price
#                     sell_stock += biggest_price
#                     profit += sell_stock - buy_stock
#                     print(f'sell : {sell_stock}')
#                     print(f'buy : {buy_stock}')
#                     return profit


######### FINAL CODEEEEEEEEEEEEEEEE############
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
result2 = sol.maxProfit([20, 30, 1, 45, 60])
result3 = sol.maxProfit([7, 6, 4, 3, 2])
print(f'result of first array : {result}')
print(f'result of second array : {result2}')
print(f'result of third array : {result3}')


############ ORIGINAL CODEEEEEEEEEEEEEEEEE###############
# class Solution(object):
#     def maxProfit(self, prices):

#         max_price = 0
#         min_price = prices[0]
#         min_price_index = 0
#         profit = 0

#         for i in range(len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#                 min_price_index = i

#         for x in range(len(prices)):
#             if (prices[x] > max_price) and (x > min_price_index):
#                 max_price = prices[x]
#                 profit = max_price-min_price
#         # profit = max_price-min_price
#         return profit


# sol = Solution()
# result = sol.maxProfit([7, 1, 5, 3, 6, 4])
# result2 = sol.maxProfit([20, 30, 1, 45, 60])
# result3 = sol.maxProfit([7, 6, 4, 3, 1])
# print(f'result of first array : {result}')
# print(f'result of second array : {result2}')
# print(f'result of third array : {result3}')
