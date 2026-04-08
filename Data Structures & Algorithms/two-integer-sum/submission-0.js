class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const charMap = {};

        for (let i = 0; i < nums.length; i++) {
            const a = target - nums[i];
            if (a in charMap) {
                return [i, charMap[a]];
            }

                        charMap[nums[i]] = i;

        }

        return [];
    }
}
