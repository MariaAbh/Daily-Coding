# 138
# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

def nb_coin(n):
    if n == 0:
        return 0
    if n < 0:
        return float('inf')
    return min(1+nb_coin(n-1), 1+nb_coin(n-5), 1+nb_coin(n-10), 1+nb_coin(n-25))

print(nb_coin(26))
