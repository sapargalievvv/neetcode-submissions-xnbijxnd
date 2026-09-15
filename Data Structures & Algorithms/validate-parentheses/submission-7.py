class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closings = {"}": "{", "]": "[", ")": "("}

        for ch in s:
            if ch in closings:
                if stack:
                    peak = stack.pop()
                    if peak != closings[ch]:
                        return False
                else: 
                    return False
            else:
                stack.append(ch)

        print("stack", stack)
        return not stack
