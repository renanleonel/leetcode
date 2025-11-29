class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0

        for word in words:
            x = True
            for letter in word:
                if letter not in allowed:
                    x = False
                    break

            if x == True:
                consistent += 1
        
        return consistent