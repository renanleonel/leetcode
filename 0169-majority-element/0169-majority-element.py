class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        element = 0
        occurrences = 0

        for k, v in hashmap.items():
            if v >= occurrences:
                occurrences = v
                element = k

        return element