class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for str in strs:
            count = [0] * 26
            
            for c in str:
                count[ord('z') - ord(c)] += 1

            key = tuple(count)

            if key in res:
                res[key].append(str)
            else:
                res[key] = [str]

        return list(res.values())