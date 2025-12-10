class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                ans += n
            else:
                ans -= n

        return ans