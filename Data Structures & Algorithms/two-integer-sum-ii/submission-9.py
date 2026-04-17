class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(numbers):
            if num in h:
                    return [h[num]+1, i+1]
            else:
                h[target-num] = i