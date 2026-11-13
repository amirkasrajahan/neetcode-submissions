class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0
        for price in prices:
            lowest = min(price, lowest)
            best = max(best, price - lowest)
        return best
