#day5
#question13
#question link=https://leetcode.com/problems/single-number/
----------------------------------------

#solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_nums=sum(set(nums))*2
        #print(set_nums)
        sum_nums=sum(nums)
        return set_nums-sum_nums
        
        
