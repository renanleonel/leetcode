class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []

        for o in order:
            if o in friends:
                ans.append(o)
        
        return ans