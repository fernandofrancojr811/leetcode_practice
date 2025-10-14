class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #first we are going to have an array result and were going to initialize this with 1 * lenght of the nums array
        res = [1] * (len(nums))

        #we will them set a prefix at 1 for a placeholder before the spot

        prefix = 1

        for i in range(len(nums)): #for every number in the length of the nums array
            res[i] = prefix # we will set result array to the prefix
            prefix *= nums[i] #we will them mulitply the prefix by the num in nums array at that index
        postfix = 1 #now we pass through it again but in reverse and set a postfix
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix #we set the result array at index to be multipled by the postfix
            postfix *= nums[i] #we will them mulitply the postfix by the num in nums array at that index
        return res