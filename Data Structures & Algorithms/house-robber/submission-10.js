class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        if (nums.length < 2){
            return Math.max(...nums)
        }
        let dp = new Array(nums.len).fill(0);
        dp[0] = nums[0];
        dp[1] = Math.max(dp[0], nums[1])

        for (let i = 2; i < nums.length; i++) {
            const rob = nums[i] + dp[i - 2];
            const notRob = dp[i - 1]

            dp[i] = Math.max(rob, notRob)
        }

        console.log(dp)
        return Math.max(...dp);
    }
}
