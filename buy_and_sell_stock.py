"""
in this problem we will track the cheap day to buy stock and a high stock profit price day to sell it
we are using 2 pointer to track the min day and max profit in a single scan so time complexity is O(n) and space is O(1) there is no extramemory used here


"""
def max_profit_stock(prices):
    left,right=0,1 #buy 
    max_profit=0
    for right in range(1,len(prices)):
        if prices[left]>prices[right]:
            left=right
        else:
            profit=prices[right]-prices[left]
            max_profit=max(max_profit,profit)
    return max_profit


prices=[10,1,5,6,7,1]
print(max_profit_stock(prices))
