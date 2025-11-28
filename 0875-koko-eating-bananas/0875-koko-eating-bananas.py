class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)
        minRate = 0

        while l <= r:
            mid = math.ceil((r + l) / 2)
            hours = 0

            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                minRate = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minRate