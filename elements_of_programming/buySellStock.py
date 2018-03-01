array = [310,315,275,295,260,270,290,230,255,250]

def maxProfit(prices):
    '''
    inputs:
    `prices` - list of integers corresponding to stock prices

    returns:
    `max_profit` (int) - maximum max_profit in the array
    '''

    # keep track of current profit
    max_profit = 0

    # keep track of minimum price seen so far while traversing the array
    # a valid profit only occurs when a stock is bought cheaply and then sold for more expensive
    min_price_seen = float('Inf')

    for price in prices:
        # compute curr profit
        curr_profit = price - min_price_seen
        max_profit = max(max_profit, curr_profit)
        min_price_seen = min(min_price_seen, price)

    return max_profit

print(maxProfit(array))
