def max_subarray_sum(l):
  continous_sum = []
  c_sum = 0
  for i in l:
    c_sum += i
    continous_sum.append(c_sum)

  min_continous_sum = []
  mc_sum = 0
  for j in continous_sum:
    if j < mc_sum:
      mc_sum = j
    min_continous_sum.append(mc_sum)

  max_sum = 0
  for z in range(len(l)):
    diff = continous_sum[z]-min_continous_sum[z]
    if max_sum < diff:
      max_sum = diff
  return max_sum

l1 = [-2, -3, -1, -2]
l2 = [-1, -3, 5, -4, 3, -6, 9, 2]
l3 = [1, 2, 3, 4, -6, 4, 5, -12]
l4 = [-1,-3,5]
l5 = [1,2]
l6 = [2,1,4]
l7 = [-1,1,2]
print(l1, '--> max:', max_subarray_sum(l1))
print(l2, '--> max:', max_subarray_sum(l2))
print(l3, '--> max:', max_subarray_sum(l3))
print(l4, '--> max:', max_subarray_sum(l4))
print(l5, '--> max:', max_subarray_sum(l5))
print(l6, '--> max:', max_subarray_sum(l6))
print(l7, '--> max:', max_subarray_sum(l7))
