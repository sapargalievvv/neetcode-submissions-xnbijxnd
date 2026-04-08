class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let result = 0
        let left = 0
        let right = 0

        while (right < prices.length) {
            let profit = prices[right] - prices[left]

            if(prices[left] > prices[right]){
                left = right
            }else{
                result = Math.max(profit, result)
            }

            right++
        }



        return result
    }
}
