#question-link=https://leetcode.com/problems/hamming-distance/

----------------------------------------------------------------------
#solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        while(x or y):
            ans=ans+(x%2^y%2);
            x=x>>1;
            y=y>>1;
        return ans
       
       
       
-----------------------------------------------------------------------------------------

in c=


int hammingDistance(int x, int y){
    int ans=0;
    while(x>0||y>0)
    {
        ans=ans+(x%2^y%2);
        x=x>>1;
        y=y>>1;
    }
    return ans;

}
