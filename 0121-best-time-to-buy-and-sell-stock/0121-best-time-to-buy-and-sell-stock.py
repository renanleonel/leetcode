class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        _max = 0

        while l < r and r <= len(prices) - 1:
            diff = prices[r] - prices[l]
            _max = max(_max, diff)

            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1

        return _max