class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listS = list(s)
        l, r = 0, 0
        hashmap = {}
        longest = 0

        while r < len(listS):
            if listS[r] in hashmap:
                hashmap.pop(listS[l])
                l += 1
            else:
                hashmap[listS[r]] = True
                diff = r - l
                longest = max(longest, diff + 1)
                r += 1

        return longest