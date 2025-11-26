class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if i == 0:
                stack.append((i, t))
            else:
                if temperatures[i] <= temperatures[i - 1]:
                    stack.append((i, t))
                else:
                    while stack and stack[-1][1] < temperatures[i]:
                        days = i - stack[-1][0]
                        ans[stack[-1][0]] = days
                        stack.pop()

                    stack.append((i, t))
        return ans
