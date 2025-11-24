class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numsSet = set(nums)

        for num in numsSet:
            count = 0
            if num - 1 not in numsSet:
                n = num
                while n in numsSet:
                    count += 1
                    n += 1

                ans = max(ans, count)

        return ans