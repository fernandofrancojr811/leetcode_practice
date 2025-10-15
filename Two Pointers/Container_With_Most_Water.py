# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         res = 0
#         l, r = 0, len(heights) -1

#         while l < r:
#             area = (r-l)* min(heights[l], heights[r])
#             res = max(res, area)

#             if heights[l] < heights[r]:
#                 l += 1
#             else: r -= 1
#         return res 
class Solution:
    def maxArea(self, heights: List[int]) -> int:


        #step 1

        n = len(heights)
        l, r = 0, n - 1 
        maxArea = 0

        while l < r:  # while r has not crossed over left
            w = r - l # we set our width of the container
            h = min(heights[l], heights[r]) # we set our height of the container
            a = h * w # finally we find the area of the container
            maxArea = max(a, maxArea) # now that we have the most updated area we check to see
                                      # which of the 2 is greater

            if heights[l] < heights[r]: # here we want to check which of the bars is taller to keep that one
                l += 1
            else:
                r-=1
        #finally we return the largest area we can find
        return maxArea

        #Time => O(n) n being each bar
        #Space => O(1) we never store anything so 
