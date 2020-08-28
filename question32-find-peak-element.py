#day11
#question-link=https://leetcode.com/problems/find-peak-element/
---------------------------------------------------------------------------------
#solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]<nums[i-1]):
                continue;
            else:
                return i
        
