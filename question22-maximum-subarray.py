#day8
#question_link=https://leetcode.com/problems/maximum-subarray/

--------------------------------------------------------------------------
#solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current=max_global=nums[0]
        for i in range(1,len(nums)):
            max_current=max(nums[i],max_current+nums[i])
            if(max_current>max_global):
                max_global=max_current
        return max_global
        
