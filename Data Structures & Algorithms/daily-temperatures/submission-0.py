class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  
        res = [0]*len(temperatures)

        stack.append(0)

        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1] 
                stack.pop()
            
            stack.append(i)

        return res