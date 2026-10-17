class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '/', '*']
        stack = []

        for token in tokens:
            result = 0
            
            if token in operations:
                if token == '+':
                    result = stack[len(stack) - 2] + stack[len(stack) - 1]
                elif token == '-':
                    result = stack[len(stack) - 2] - stack[len(stack) - 1]
                elif token == '/':
                    result = int(stack[len(stack) - 2] / stack[len(stack) - 1])
                elif token == '*':
                    result = stack[len(stack) - 2] * stack[len(stack) - 1]
                
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))
            
        return stack[len(stack) - 1]