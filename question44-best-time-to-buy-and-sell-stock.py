#question-link=https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

________________________+++++++++++++++++++++++________________+++++++++++++++_____________________+++++++++++++++++

#solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        priceLen = len(prices)
        
        if priceLen == 0:
            return 0
        
        maxProfit = 0
        minPrice = prices[0]
        
        for i in range(1, priceLen):
            
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            
        return maxProfit
