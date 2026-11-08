class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                res = 0

                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == "*":
                    print(a,b)
                    res = a * b
                else:
                    res = int(a / b)

                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]