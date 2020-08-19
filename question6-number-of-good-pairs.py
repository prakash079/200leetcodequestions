#question6
#question link=https://leetcode.com/problems/number-of-good-pairs/

------------------------------------------

#solution

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hasht=[0]*101
        count=0
        for i in nums:
            hasht[i]+=1
        count=0
        for i in range(101):
            count=count+((hasht[i]*(hasht[i]-1))//2)
        return count
