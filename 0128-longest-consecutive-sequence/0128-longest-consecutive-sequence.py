class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numsSet = set(nums)

        for num in numsSet:
            count = 0
            if num - 1 not in numsSet:
                i = num
                while i in numsSet:
                    count += 1
                    i += 1

                if count >= ans:
                    ans = count

        return ans

        