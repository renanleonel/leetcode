class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        ans = []

        for word in s1.split(' '):
            hashmap[word] = 1 + hashmap.get(word, 0)

        for word in s2.split(' '):
            hashmap[word] = 1 + hashmap.get(word, 0)

        for k, v in hashmap.items():
            if v == 1:
                ans.append(k)
                
        return ans