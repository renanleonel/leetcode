class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        x = 0

        for i, n in enumerate(nums):
            if n == 1:
                if i == 0:
                    continue
                elif x < k:
                    return False
                else:
                    x = 0
            else:
                x += 1

        return True