#question_link=https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


----------------------------------------------------------------------------------------------
#solution=
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        l=0
        r=len(nums)-1

        while l<=r and l<len(nums)-1 and r>0:
            if nums[l]!=target:
                l+=1
            if nums[r]!=target:
                r-=1
            if nums[l]==target and nums[r]==target:
                break
        if nums[l]==target:
            return [l,r]
        else:
            return [-1,-1]
