class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        result = 0

        while l < r:
            factor = min(height[l], height[r])
            diff = r - l

            result = max(result, factor * diff)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
            
    
        