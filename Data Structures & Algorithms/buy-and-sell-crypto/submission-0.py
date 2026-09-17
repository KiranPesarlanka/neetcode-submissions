class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0
        minv = prices[0]

        for p in prices:
             minv = min(p, minv)
             maxp = max(p-minv, maxp)

        return maxp