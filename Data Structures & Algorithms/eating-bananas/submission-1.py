class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2
            hours_sum = 0
            for bananas in piles:
                hours_sum += (bananas + mid - 1) // mid

            if hours_sum <= h:
                right = mid
            else:
                left = mid + 1

        return left