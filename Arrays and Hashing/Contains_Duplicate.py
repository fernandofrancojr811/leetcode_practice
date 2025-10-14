class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set() # we first initialize a set

        for num in nums: # for every number in the nums array
            if num in seen: # we check if its in the array
                return True # if it is re return true because
            else:
                seen.add(num) # if it have not been seen we add it to the set and repeat
        return False #we return false because this means that we never saw a duplicate


        #Time Complexity => O(n) n being the number of elements in nums array
        #Space Complexity => O(n) because we are storing a set with n elements
        