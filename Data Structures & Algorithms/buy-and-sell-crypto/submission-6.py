class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        res = 0 

        while right < len(prices):
            profit = prices[right] - prices[left]
            res = max(res, profit)

            if prices[left] > prices[right]:
                left = right
            
            right += 1


        return res