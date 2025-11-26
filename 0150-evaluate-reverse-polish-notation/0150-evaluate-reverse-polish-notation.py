class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                a, b = int(stack.pop()), int(stack.pop())
                c = b + a
                stack.append(c)
            elif token == '-':
                a, b = int(stack.pop()), int(stack.pop())
                c = b - a
                stack.append(c)
            elif token == '*':
                a, b = int(stack.pop()), int(stack.pop())
                c = b * a 
                stack.append(c)
            elif token == '/':
                a, b = int(stack.pop()), int(stack.pop())
                c = b / a
                stack.append(c)
            else:
                stack.append(token)

        return int(stack[0])