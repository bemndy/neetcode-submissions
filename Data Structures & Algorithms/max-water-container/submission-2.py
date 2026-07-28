class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # initialize everything
        l = 0 
        r = len(heights) - 1
        max_amount = 0

        while l < len(heights) - 1:
            # check if new max amount
            current_amount = (r - l) * min(heights[l], heights[r])
            if max_amount < current_amount:
                max_amount = current_amount

            #check if l is smaller than r
            if heights[l]< heights[r]:
                l += 1
                r = len(heights) - 1
                continue
        
            # decrement r
            r -= 1

            # check if l needs to be incremented
            if r == l:
                r = len(heights) - 1
                l += 1

        return max_amount
            