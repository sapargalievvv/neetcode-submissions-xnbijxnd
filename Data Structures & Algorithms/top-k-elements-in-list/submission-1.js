class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numsCountMap = new Map();

        for (const num of nums) {
            numsCountMap.set(num, (numsCountMap.get(num) || 0) + 1);
        }

        const descSorted = [...numsCountMap.entries()].sort((a, b) => {
            return b[1] - a[1];
        });

        return descSorted.slice(0, k).map((n) => n[0]);
    }

}