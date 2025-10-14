class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        h = {} #first we set up a list

        for i in range(len(nums)): # for each item in the lenght of the nums array
            h[nums[i]] = i #we set h at nums[i] to be equal to i, this mean we have all of the values in a list

        for i in range(len(nums)): #we then iterate through the array again but this time
            y = target - nums[i] #we are looking for a number when subracted from the target equals y

            if y in h and h[y] != i: # we then can say if we find y inside of the set and h[y] is not equal to the 
                return[i, h[y]]  #current index we are on then we can return the list of i, and h[y]
        