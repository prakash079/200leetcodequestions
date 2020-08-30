#link = =https://leetcode.com/problems/reverse-string/

-----------------------------------------------------------------
#solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = len(s)
        i = 0
        while i < (l//2):
            s[i],s[l-i-1] = s[l-i-1],s[i]
            i += 1
