class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        ans = []
        
        for h, n in zip(heights, names):
            hashmap[h] = n

        for h in reversed(sorted(heights)):
            ans.append(hashmap[h])

        return ans