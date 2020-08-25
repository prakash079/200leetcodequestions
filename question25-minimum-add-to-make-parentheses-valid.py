#day9
#question-link=https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

-------------------------------------------------------------------------------------------------
#solution
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack =0
        count = 0
        for c in S:
            if c == '(':
                stack += 1
            elif stack > 0:
                stack -= 1    
            else:
                count += 1
        return stack + count
