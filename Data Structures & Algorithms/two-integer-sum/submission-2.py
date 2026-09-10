class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums):            
            diff = target - num
            
            if diff in numsDict:
                return [numsDict[diff], i]
            
            numsDict[num] = i


        return []