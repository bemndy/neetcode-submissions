class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(numbers):
            print(num, target-num)
            if num in h:
                print("i got to this point")
                if abs(num) >= abs(h[num]):
                    return [h[num]+1, i+1]
            else:
                h[target-num] = i