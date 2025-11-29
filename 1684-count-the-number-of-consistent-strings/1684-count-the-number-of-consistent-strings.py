class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = len(words)

        for word in words:
            for letter in word:
                if letter not in allowed:
                    consistent -= 1
                    break

        return consistent