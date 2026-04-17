class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # we have to sort, in order to remove duplicates
        # i thought we just removed the first index, which is good intuition

        # but if you get a combo: a + b + c == 0
        # we need to make sure a doesn't show up again (left to right)
        # so we make it sorted

        # we can prevent this by asking what time complexity has to be

        # O(nlogn)
        nums.sort()


        # two for loops O(n^2)
        for i, num in enumerate(nums):

            # this is the duplicate condition check 
            # use complex conditionals if you have to (i > 0)
            if i > 0 and num == nums[i-1]:
                continue

            # the left and right pointer are the one after i
            # nums[i] becomes the target, then just twosum
            l, r = i + 1, len(nums) - 1

            # two sum II used a left and right pointer, I used a hashmap
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:

                    # add a combo
                    res.append([num, nums[l], nums[r]])

                    # add one more to left 
                    # and then use while loop to check for duplicates
                    # this makes the code more efficient
                    # we can remove old cases, in case (a) could go with another (b, c)
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                

             
            
                
            

        