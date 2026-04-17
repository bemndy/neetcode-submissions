import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            product = math.prod(nums[:i]) * math.prod(nums[i+1:])
            output.append(product)
        return output