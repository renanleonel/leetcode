class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = n % 2
        return sorted(nums)