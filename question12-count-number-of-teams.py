#question12
#link=https://leetcode.com/problems/count-number-of-teams/

-------------------------------------------------------------------------------------------------
#solution
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        n=len(rating)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if((rating[i]<rating[j] and rating[j]<rating[k]) or (rating[i]>rating[j] and rating[j]>rating[k])):
                        count+=1
        return count
