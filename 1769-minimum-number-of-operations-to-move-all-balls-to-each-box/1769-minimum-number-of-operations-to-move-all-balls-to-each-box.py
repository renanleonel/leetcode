class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        balls, moves = 0, 0

        for i in range(len(boxes)):
            ans[i] += balls + moves
            moves += balls
            balls += int(boxes[i])

        balls, moves = 0, 0

        for j in range(len(boxes) - 1, -1, -1):
            ans[j] += balls + moves
            moves += balls
            balls += int(boxes[j])

        return ans