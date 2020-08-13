#question11
#link=https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

--------------------------------------------------------------

#solution

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        q=queryTime
        c=0
        for i in range(len(startTime)):
            if(q>=startTime[i] and q<=endTime[i]):
                c+=1
        return c
