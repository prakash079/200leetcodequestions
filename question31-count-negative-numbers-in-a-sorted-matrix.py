#question-link=https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


-----------------------------------------------------------------------------------------------------------
#solution

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        count=0
        for i in grid:
            if(i[-1]<0):
                count+=len(i)
            elif(i[0]>=0):
                continue
            else:
                n=len(i)
                j=0
                while(j<n):
                    if(i[j]>=0):
                        break
                    else:
                        count+=1
                        j+=1
        return count
