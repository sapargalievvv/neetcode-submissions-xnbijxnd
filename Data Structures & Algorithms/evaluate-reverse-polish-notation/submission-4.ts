class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stack = [];

        for (const token of tokens) {
            if (["+", "-", "*", "/"].includes(token)) {
                const b = stack.pop();
                const a = stack.pop();

                if (token === "+") {
                    stack.push(a + b);
                } else if (token === "-") {
                    stack.push(a - b);
                } else if (token === "*") {
                    stack.push(a * b)
                } else {
                    stack.push(Math.trunc(a / b))
                }
            } else {
                stack.push(parseInt(token));
            }
        }
        
        
        return stack[0]
    }
}
