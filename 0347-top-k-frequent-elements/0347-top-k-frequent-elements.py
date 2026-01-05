class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)

        for number, occurence in hashmap.items():
            frequency[occurence].append(number)

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                ans.append(n)

                if len(ans) == k:
                    return ans