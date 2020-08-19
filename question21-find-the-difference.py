#question-link=https://leetcode.com/problems/find-the-difference/
------------------------------------------------------------------------------

#solution
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
