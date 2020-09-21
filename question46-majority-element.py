#link=https://leetcode.com/problems/majority-element/

-------------------------------------------------
#solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for a in set(nums):
            if nums.count(a) > len(nums) / 2:
                return a
