class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for n in nums:
            total += n
        return total % k