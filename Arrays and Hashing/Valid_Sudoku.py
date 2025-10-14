class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       #Row
       #O()

        for i in range(9):# this is because the board is 9x9
            s = set() # we make a set for each row to check each row
            for j in range(9):
                item = board[i][j] # this is for each specific grid tile
                if item in s:
                    return False #if the item has already been seen in that space return false
                elif item != '.':
                    s.add(item) #we add item to the set



       #Cols (the exact same as rows but we are checking [j][i]
        for i in range(9): # this is because the board is 9x9
            s = set() # we make a set for each row to check each row
            for j in range(9):
                item = board[j][i] # this is for each specific grid tile
                if item in s:
                    return False #if the item has already been seen in that space return false
                elif item != '.':
                    s.add(item) #we add item to the set
        





       # 3x3 Boxes
       # What we need to under stand is that there are specific tiles
       # on the map where our count to validate can start
       # this is at the top left of every box

       #we initialize a set containing the starts
        starts= [ (0,0), (0,3), (0,6),
                 (3,0), (3,3), (3,6),
                 (6,0), (6,3), (6,6)]

        for i,j in starts: #for each starting postition
            s = set(); # we make a set like before
            for row in range(i, i+3): #iterate withing the boxs rows
                for col in range(j, j+3):#iterate withing the cols
                    item = board[row][col] #now we set each item to be board row at col
                    if item in s:
                        return False
                    elif item != '.': #if the item isnt a . then we add it to the set
                        s.add(item)
        return True



        