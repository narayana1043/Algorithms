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

for j in coin_values:
    print(j)
    for i in range(S+1):
        # if using just the coin 1 what are the possible best solution and update as you see new coins
        if min_coins[i] != math.inf and i + j <= S:
            min_coins[i + j] = min(min_coins[i + j], min_coins[i] + 1)
            print(min_coins)

print([i for i in range(S+1)])
print(min_coins)
