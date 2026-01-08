class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        _max = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            _max = max(_max, profit)

            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1

        return _max