class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        _max = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            _max = max(_max, diff)

            if prices[r] < prices[l]:
                l = r
            r += 1

        return _max