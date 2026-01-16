class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start, self.end = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l > self.end - self.start:
                    self.start, self.end = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return s[self.start:self.end + 1]