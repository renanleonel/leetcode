class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l, r = 0, 0
        total = 0

        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            if r - l + 1 - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1

            total = max(total, r - l + 1)
            r += 1

        return total