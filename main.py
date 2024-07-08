def BestTime(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

#Example 1:
#Input: 
prices = [7,1,5,3,6,4]
print(BestTime(prices))
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#Example 2:
#Input: 
prices = [7,6,4,3,1]
print(BestTime(prices))
#Output: 0
#Explanation: In this case, no transactions are done and the max profit = 0.
