class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for ch in s:
           if ch not in closing: 
            stack.append(ch)
           else:
            isEmpty = len(stack) == 0
            if isEmpty:
                return False
            else:
                peak = stack.pop()
                if peak != closing[ch]:
                    return False

        if len(stack): 
            return False
                
        return True