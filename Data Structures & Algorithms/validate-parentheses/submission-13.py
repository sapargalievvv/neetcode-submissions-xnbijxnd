class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closing_brackets = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for bracket in s:
            if bracket in closing_brackets:
                if stack and closing_brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack