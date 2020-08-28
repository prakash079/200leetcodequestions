#question-link=https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

--------------------------------------------------------------------------
#solution

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return -1
        if(len(nums)==1):
            return nums[0];
        left=0
        right=len(nums)-1
        while(left<right):
            mid=(left+right)//2
            if(nums[mid]<nums[mid-1] and mid>0):
                return nums[mid]
            elif(nums[left]<=nums[mid] and nums[mid]>nums[right]):
                left=mid+1
            else:
                right=mid-1
        return nums[left]
            
        
