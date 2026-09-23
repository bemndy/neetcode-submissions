class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
    
        def ate(rate):
            import math
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / rate)
                      
            return num_hours <= h
        
        while left < right:
            mid = (left + right) // 2
            if ate(mid):
                right = mid
            else:
                left = mid + 1

        return left