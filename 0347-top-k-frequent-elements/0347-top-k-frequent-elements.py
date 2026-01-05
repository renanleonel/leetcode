class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for key,v in hashmap.items():
            freq[v].append(key)

        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                if len(ans) == k:
                    return ans

                ans.append(j)

        return ans