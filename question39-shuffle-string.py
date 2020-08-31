#day13
#question-link=https://leetcode.com/problems/shuffle-string/

---------------------------------------------------------------------------
#solution
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[""]*len(s)
        j=0
        for i in range(len(indices)):
            l[indices[i]]=s[i]
        #print(l)
        ans=""
        for i in range(len(s)):
            ans=ans+l[i]
        return ans
