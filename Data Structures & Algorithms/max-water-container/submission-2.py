class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0

        while left < right:
            amount = min(heights[right], heights[left]) * (right - left)
            res = max(res, amount)

            if heights[right] > heights[left]:
                left +=1 
            else: 
                right -=1




        return res 
