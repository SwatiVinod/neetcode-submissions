class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for symbol in s:
            if symbol in ['(', '{', '[']:
                stack.append(symbol)
            elif symbol == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif symbol == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif symbol == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

                

