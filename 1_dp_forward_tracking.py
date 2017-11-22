'''
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.
'''

import math

coin_values = [1, 3, 5]
N = len(coin_values)
S = 11 # sum
min_coins = [math.inf for i in range(S+1)]
min_coins[0] = 0


for i in range(1,S+1):
    for j in range(N):
        print(coin_values[j], i, min_coins[i - coin_values[j]]+1, min_coins[i])
        if coin_values[j] <= i and min_coins[i-coin_values[j]]+1 < min_coins[i]:
            min_coins[i] = min_coins[i-coin_values[j]]+1

print([i for i in range(S+1)])
print(min_coins)

