class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        l = 0
        r = n-1 # initialize the pointers at beginning and end

        while l < r: # while the pointers are not crossing over each other
            summ = numbers[l] + numbers[r] # we create a target sum
            if summ == target: #if the sum of both l and r is the target we return them +1 indexed
                return[l+1, r+1]

            elif summ < target: #if they are not equal to the sum but less then the sum
            # this means we move the left one up since the order is accending and we need
            # the total sum to go up
                l += 1
            # else in this case is if summ is greater than the target.
            # we move up the pointer r becuase the list is in accending order
            # and we need to make the sum smaller by moving to a smaller number
            else:
                r -= 1

        

                