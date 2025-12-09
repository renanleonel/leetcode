class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        
        for number in bin(n):
            if number == '1':
                ans +=1

        return ans