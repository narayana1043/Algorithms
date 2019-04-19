'''
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum
of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in
such a way that they sum up to S.
'''

import math

coin_values = [1, 3, 5]
N = len(coin_values)
S = 11 # sum
min_coins = [math.inf for i in range(S+1)]
min_coins[0] = 0


for i in range(1,S+1):
    # optimizing for each value before the finale value of S
    # optimization for the next value to depends on previous optimized value
    for j in range(N):
        # for each available coin check if it reduces min coin count for the current optimization value
        # can ignore the first condition in the if clause but including it will reduce complexity
        print(coin_values[j], i, min_coins[i - coin_values[j]]+1, min_coins[i])
        if coin_values[j] <= i and min_coins[i-coin_values[j]]+1 < min_coins[i]:
            # if true update the number of minimum number of coins required
            min_coins[i] = min_coins[i-coin_values[j]]+1

print([i for i in range(S+1)])
print(min_coins)

