 # 1636
 # e.g: waterrfetawx k = 2 -> waterretaw
 # assumption that k is less than len(s)

def check_palindrom(s):
    return s == s[::-1]

def make_palindrom(s, index, k):
    if k < 0:
        return False

    if check_palindrom(s):
        return True

    if index > len(s):
        return False

    delete = make_palindrom(s[:index]+s[index+1:] , index, k-1)
    keep = make_palindrom(s, index+1, k)

    return delete or keep

res = make_palindrom('waterrfetawx', 0, 2)
print(res)

res = make_palindrom('marma', 0, 2)
print(res)

res = make_palindrom('marmar', 0, 2)
print(res)

res = make_palindrom('titouan', 0, 2)
print(res)

res = make_palindrom('titouan', 0, 4)
print(res)
