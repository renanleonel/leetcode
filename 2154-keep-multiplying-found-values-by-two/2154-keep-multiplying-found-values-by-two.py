class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        
        for n in sorted(nums):
            if n == ans:
                ans *= 2

        return ans