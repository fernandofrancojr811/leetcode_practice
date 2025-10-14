from collections import Counter #make sure to import the library
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #First we have to get into base cases, if there is a difference in lengths they are not valid
            return False # We immediatly return false

        s_dict = Counter(s) # we set each to be a list with a key and value
        t_dict = Counter(t) 

        if s_dict == t_dict: # if each key and value pair are the exact same then we return true
            return True
        else:
            return False # if not we return false
            