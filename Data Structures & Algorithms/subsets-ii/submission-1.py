class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(path, start):
            print('path',path)
            print('start',start)

            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                bt(path, i + 1)
                path.pop()

        bt([],0)

        return res