class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numSet = set(nums)

        for n in numSet:
            if n - 1 in numSet:
                continue
            
            i = n
            count = 0
            
            while i in numSet:
                i += 1
                count += 1

            ans = max(ans, count)

        return ans