#question-link=https://leetcode.com/problems/missing-number/
_____________________________________________________________________________-

#solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        gaus_sum=n*(n+1)//2
        normal_sum=sum(nums)
        return gaus_sum-normal_sum
