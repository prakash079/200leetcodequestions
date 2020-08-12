#question8
#question link=https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

----------------------------------------

#solution

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l=[]
        while(n):
            l.append(n%10)
            n=n//10
        print(l)
        s=0
        m=1
        for i in l:
            m=m*i
            s=s+i
        return m-s
            
