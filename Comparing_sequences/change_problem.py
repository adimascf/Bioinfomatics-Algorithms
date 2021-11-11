

def dp_change(money, set_coins):
    """Finding a minimum number of coins to make change from a given change and set of coins"""
    min_num_coins = {}
    min_num_coins[0] = 0
    for m in range(1, money + 1):
        min_num_coins[m] = float('inf')
        for coin in set_coins:
            if m >= coin:
                if min_num_coins[m - coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m - coin] + 1
    return min_num_coins[money]

with open('E://rosalind//rosalind_ba5a.txt', 'r') as f:
    change_money = f.readline().strip()
    change_money = int(change_money)
    coins = f.readline().strip().split(',')
    the_coins = [int(c) for c in coins]
    print(dp_change(change_money, the_coins))