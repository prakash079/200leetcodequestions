#day12
#question-link=https://leetcode.com/problems/squares-of-a-sorted-array/

-------------------------------------------------------------
#solution
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i]=A[i]**2
        A.sort()
        return A
            
        
