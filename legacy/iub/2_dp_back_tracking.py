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

def back_track(S, V):
    count = []
    for v in V:
        V_ = [v_ for v_ in V if v_ <= S]
        if S !=0 and V_ != []:
            print(S, V_)
            # back track after choosing one of the possible ways at a hand and get the soln
            count.append(back_track(S-v, V_))
        elif S==0:
            # if the total = sum return 0
            return 0
        elif V_ == []:
            # if ran out of options return math.inf
            return math.inf
    print(count)
    print(min(count)+1)
    return min(count)+1

print(back_track(S, coin_values))

