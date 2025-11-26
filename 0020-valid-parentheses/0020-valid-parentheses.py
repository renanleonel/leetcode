class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in hashmap and stack and hashmap[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return True if len(stack) == 0 else False