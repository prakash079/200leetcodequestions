#day7
#question_link=https://leetcode.com/problems/single-number-ii/
-----------------------------------------------------------------------
#solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_set=sum(set(nums))
        sum_nums=sum(nums)
        res=(sum_set)*3-sum_nums
        return res//2
        
