class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        hashmap = {}
        l, r = 0, 0
        longest = 0

        while r < len(arr):
            if arr[r] in hashmap:
                hashmap.pop(arr[l])
                if l == r:
                    r += 1
                else:
                    l += 1
            else:
                diff = r - l
                longest = max(longest, diff + 1)
                hashmap[arr[r]] = True
                r += 1

        return longest

                



        