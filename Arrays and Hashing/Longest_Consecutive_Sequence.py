# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for n in nums:
#             # check if it is the start of a sequence
#             if (n - 1) not in numSet:
#                 length = 0
#                 while (n + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest    


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums) #create a set for O(1) look up of items

        c_longest = 0

        for num in s:
            if num - 1 not in s: # this means if our current num is not in the set
                next_num = num + 1 # we set next num to be num + 1 and increase length
                length = 1
                while next_num in s: # we then check if next num is in sett
                    length += 1 # if it is we increase the length
                    next_num += 1 #and then set next num to the number after that
                c_longest = max(c_longest, length) # once we dont see the next number in the set
                                                       # we get the max of the current longest and the current length
        return c_longest #we can then return the longest which is always guaurneteed to be the bigggest
                
        

        #Time => O(n) n being the amount of nums in the num array
        #Space is O(n) because we are storing n nums in the set we created
























