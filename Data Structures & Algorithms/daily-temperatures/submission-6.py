class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, daytemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < daytemp:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return result
