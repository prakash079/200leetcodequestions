#question15
#question link=https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

----------------------------------------------

#solution
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        while(num):
            if(num%2==0):
                num=num//2
                count+=1
            else:
                num=num-1
                count+=1
        return count
