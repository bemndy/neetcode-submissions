class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit < 0:
                left = right
            elif current_profit > max_profit:
                max_profit = current_profit
            if right == len(prices):
                left += 1
                right = left
            right += 1
        return max_profit