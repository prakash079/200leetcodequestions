#question-link=https://leetcode.com/problems/find-the-duplicate-number/

-----------------------------------------------------------------------
#solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i+1]==nums[i]):
                return nums[i]
            
        
