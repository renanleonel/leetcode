class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        l, r = 0, len(ans) - 1

        while l < r:
            if not ans[l].isalpha():
                l += 1
            elif not ans[r].isalpha():
                r -= 1
            else:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1

        return ''.join(ans)