from collections import defaultdict #first we make sure to import this and use it
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_d = defaultdict(list) #we first want to make a deafualt dict of anagrams

        for s in strs: # for every string inside of the strs array we want to initialize a new array the size
            count = [0] * 26 # of 26 0's, one for every letter of the alphabet

            for c in s: #next for every character in s we want to set each count at the letter it is to increment by 1
                count[ord(c) - ord('a')] += 1

            key = tuple(count) #we now set a key to be the tuple of count since lists are imutable but tuples are not
            anagram_d[key].append(s) #we then for this key in anagram_d we append string s.

        return list(anagram_d.values()) #in the end we return the values in the anagrams dictionary because thats exactly
                                        #what we want to be output