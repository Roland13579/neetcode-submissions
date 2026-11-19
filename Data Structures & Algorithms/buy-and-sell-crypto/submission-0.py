class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #DP problem
        # profit would be current price - lowest we have seen so far
        minBuy = -1 # First price
        maxP = 0 # Best profit
        
        for i in range(len(prices)):
            if (minBuy == -1 or minBuy>prices[i]):
                print("minBuy:", minBuy, "prices[i]:", prices[i])
                minBuy = prices[i]
                print("new minBuy:", minBuy)
            maxP = max(maxP,prices[i] - minBuy)
            print("maxP: ", maxP)
        return maxP