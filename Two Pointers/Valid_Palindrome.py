# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s)-1

#         while l < r:
#             while l < r and not self.alphaNum(s[l]):
#                 l +=1
#             while r > l and not self.alphaNum(s[r]):
#                 r -=1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1
#         return True


#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9'))

class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s) # we first start off by making sure we have 2 poniters

        l = 0
        r = n-1

        while l < r: #while the right pointer is not further left than the left
            if not s[l].isalnum(): #we can say if l is not an alphanum char then we move it
                l += 1
                continue
            if not s[r].isalnum(): #same with r
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): #if the pointers are now at valid chars but are not the same char
            # we return false
                return False
            #but if they are the same we increment both and start the loop over
            
            l += 1
            r -= 1
            #once we break out this successfully means l and r are i the same posistion and all
            # chars were equal so we return true
        return True

        #time is o(n) where n is the number of characters in the string
        #Space = o(1) we are not using and storage
     


