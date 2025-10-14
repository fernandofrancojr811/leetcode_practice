class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = "" # first we initialize an empty string
        for s in strs: # for every string in the strs array we want to
            encoded += str(len(s)) + "#" + s # add the length of s as a string + a deleimeter + s itself
        return encoded # this encode is easy
            

    def decode(self, s: str) -> List[str]:

        decoded = []  # here we have the new array of words that will be decoded and the
        i = 0
        while i < len(s): # s is the new long string we have so we use a pointer to signify the beginning
            j = i # we set a new pointer to iterate over the string at the beginning as well
            while s[j] != "#": # while j is not at the delimiter we increment it
                j+= 1
            length = int(s[i:j]) #we then can set the 
            decoded.append(s[j+1 : j + 1 + length])
            i = j + 1 + length # we set i to be after the end of the length of the last string
        return decoded