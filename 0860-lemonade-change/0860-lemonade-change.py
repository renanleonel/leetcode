class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            else:
                if b == 10:
                    if fives == 0:
                        return False
                    else:
                        fives -= 1
                        tens += 1
                else:
                    if tens >= 1 and fives >= 2:
                        tens -= 1
                        fives -= 2
                    elif fives >= 3:
                        fives -= 3
                    else:
                        return False
        return True