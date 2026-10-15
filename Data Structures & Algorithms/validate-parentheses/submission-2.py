class Solution:
    def isValid(self, s: str) -> bool:
        openings = ['{', '[', '(']
        stack = []
        for ch in s:
            if ch in openings:
                stack.append(ch)
            else:
                if(len(stack) == 0): 
                    return False

                head = stack[-1]
                if head == '{' and ch == '}':
                    stack.pop()
                elif head == '(' and ch == ')':
                    stack.pop()
                elif head == '[' and ch == ']':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0