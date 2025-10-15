class Solution:
    def trap(self, height: List[int]) -> int:
        #step 1: we initialize the left wall and right wall heights
        l_wall = 0 
        r_wall = 0

        #step 2 we get store a length var for simplicity
        n = len(height)

        #step 3 we set 2 array filled with n many zeros
        # we do this because in our algorithm we are going
        # to take the min of each position at each array index
        # this give us our potential water that we can store

        maxLeft = [0] * n
        maxRight = [0] * n
        # step 4 we iterate throught the heights array and fill the max arrays
        
        for i in range(n):
            j = -i -1 # this iterates backwards through the array
            maxLeft[i] = l_wall
            maxRight[j] = r_wall

            #this builds up our left and right wall arrays fully
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        #step 5
        summ = 0
        for i in range(n):
            pot = min(maxLeft[i], maxRight[i])
            # we only want to increment out sum if the potential is postive
            # sum goes up by either the max of 0 or the max of the potential water
            # stored here - the height for any blocks in the way
            summ += max(0, pot - height[i])
        
        return summ

        #Time => O(n) we go through the array a couple of times
        #Space => O(n) 
