#question-link=https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

#solution
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins=0
        n=len(piles)
        n=n//3
        j=len(piles)
        j=j-2
        for i in range(n,0,-1):
            max_coins+=piles[j]
            j=j-2
        return max_coins
