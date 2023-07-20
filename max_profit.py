class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                diff = prices[sell] - prices[buy]
                max_profit = max(max_profit, diff)
            else:
                buy = sell
            sell += 1
        
        return max_profit
    