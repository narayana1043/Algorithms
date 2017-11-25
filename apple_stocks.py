"""
Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1
purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must
pass).
"""

# Test cases
# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
# stock_prices_yesterday = [10, 11, 3, 5, 9, 7, 10, 3, 11]
# stock_prices_yesterday = [1,2,3,4,5,6,7,8,9]
# stock_prices_yesterday = [10,9,8,7,6,5,4,3,2,1]
# stock_prices_yesterday = [11, 10, 7, 5, 8, 9]
stock_prices_yesterday = [29, 10, 24, 7, 5, 8, 18, 11]

#####################################################################################################################
# Method nlogn: doesnot give the min loss (at least not yet)

def solve(x, y):
    # print(x, y)
    if len(x) == 1:
        return 0
    elif len(x) == 2:
        profit = x[1] - x[0]
        if profit > 0:
            return profit
        else:
            return 0
    elif x.index(y[0]) < x.index(y[-1]):
        return y[-1] - y[0]
    else:
        x1 = x[:x.index(y[0])]
        y1 = sorted(x1)
        x2 = x[x.index(y[0]):]
        print(x1,x2)
        y2 = sorted(x2)
        profit1 = solve(x1, y1)
        profit2 = solve(x2, y2)
        return max(profit1, profit2)

def get_max_profit_nlogn(x):
    y = sorted(x)
    return solve(x, y)

#####################################################################################################################
# Method O(n): also gives min loss

def get_max_profit_n(x):
    r_minimum = x[0]
    r_profit = x[1] - x[0]
    for i in range(1, len(x)):
        print(r_minimum, r_profit)
        potential_profit = x[i] - r_minimum
        r_profit = max(r_profit, potential_profit)
        r_minimum = min(r_minimum, x[i])

    return r_profit



#####################################################################################################################
print('O(nlogn)')
print(get_max_profit_nlogn(stock_prices_yesterday))
print('O(n)')
print(get_max_profit_n(stock_prices_yesterday))
