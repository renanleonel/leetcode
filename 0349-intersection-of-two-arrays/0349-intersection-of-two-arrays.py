class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        ans = []

        for n in nums2:
            if n in set1 and n not in ans:
                ans.append(n)

        return ans