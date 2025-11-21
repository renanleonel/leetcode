class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        if len(height) == 0:
            return water

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                water += max(maxL - height[l], 0)

            else: 
                r -= 1
                maxR = max(maxR, height[r])
                water += max(maxR - height[r], 0)

        return water