class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # sett = []
        # count = 1

        # for c in s:
        #     sett.append()

        # current = sett[0]
        # iterator = sett[1]
        
        # for c in sett:
        #     if ord(c-1) in sett:
        #         continue
        #     else: 
        #        if ord(c+1) is in sett:
        #         iterator += 1

        l = 0
        longest = 0
        sett = []
        n = len(s)
        
        #Needs to be a linear solution
        for r in range(n):
            #make sure our window is valid
            while s[r] in sett: # this means we are invalid so we need to make it valid
                sett.remove(s[l]) # we do this by removing s[l] (since its causing the duplicate then incrementing l to the next value )
                l += 1
            #now once we have a valid window we break out of the loop and calculate the window length
            window = (r-l) + 1

            #finally if our current window length is greater than our previous longest then we update it with the max() function
            longest = max(longest, window)
            # and finally we add s[r] to the set and restart
            sett.append(s[r])

        return longest