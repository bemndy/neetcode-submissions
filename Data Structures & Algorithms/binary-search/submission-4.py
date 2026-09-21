class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        midpoint = 0
        while low <= high:
            middle = (low + high) // 2
            midpoint = nums[middle]
            if midpoint == target:
                return middle
            elif midpoint > target:
                high = middle - 1 
            else:
                low = middle + 1

        return -1