#question2
#question link=https://leetcode.com/problems/shuffle-the-array/

---------------------------
#solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(0,n):
            
            l.append(nums[i])
            l.append(nums[n+i])
        return l   
