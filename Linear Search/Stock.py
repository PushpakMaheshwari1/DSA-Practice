def maxProfit(prices, n):
    buy = prices[0]
    max_profit = 0
    for i in range(1, n):
 
        ## Checking for lower buy value
        if (buy > prices[i]):
            buy = prices[i]
            print('buy',buy)
 
        ## Checking for higher profit
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
            print('max',max_profit)
    return max_profit
 
prices = [0,1,2,3,4,5,6,7,8]
n = len(prices)
max_profit = maxProfit(prices, n)
print(max_profit)