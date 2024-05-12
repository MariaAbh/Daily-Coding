# 1703
# L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

def get_cuml_sum(l):
    cumulative_sum = []
    cumulated = 0
    for nb in l:
        cumulated += nb
        cumulative_sum.append(cumulated)
    return cumulative_sum

def my_sum(l):
    c = get_cuml_sum(l)
    def mk_sum(i,j):
        return c[j-1] - c[i-1]
    return mk_sum

l = [1,2,3,4,5]
sum = my_sum(l)

assert(sum(1,3) == 5)
