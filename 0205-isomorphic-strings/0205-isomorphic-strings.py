class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS, hashmapT = {}, {}

        for i in range(len(s)):
            if (s[i] in hashmapS and hashmapS[s[i]] != t[i]) or (t[i] in hashmapT and hashmapT[t[i]] != s[i]):
                return False

            hashmapS[s[i]] = t[i]
            hashmapT[t[i]] = s[i]
        
        return True