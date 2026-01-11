class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        max_global = float('-inf') 
        max_local = 0
        for n in nums:
            max_local = max(n, max_local + n)
            max_global = max(max_global, max_local)

        return max_global