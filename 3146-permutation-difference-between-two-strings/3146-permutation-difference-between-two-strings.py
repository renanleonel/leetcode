class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        hashS, hashT = {}, {}

        for i, letter in enumerate(s):
            hashS[letter] = i

        for i, letter in enumerate(t):
            hashT[letter] = i

        for letter in s:
            ans += abs(hashS[letter] - hashT[letter])

        return ans