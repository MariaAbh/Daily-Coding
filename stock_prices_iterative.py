def iterative(l):
	max_profit = list()
	local_min = list()
	past_min = l[0]

	for i in range(len(l)):
		current_number = l[i]
		if current_number < past_min:
			past_min = current_number
		local_min.append(past_min)
		max_profit.append(current_number-local_min[i])
	return local_min[max_profit.index(max(max_profit))]

def iterative_no_list(l):
	past_min = l[0]
	local_min = past_min
	max_profit = 0
	for current_number in l:
		if current_number < local_min:
			local_min = current_number
		current_profit = current_number - local_min
		if max_profit <= current_profit:
			max_profit = current_profit
			past_min = local_min
	return past_min

l = [9, 11, 8, 16, 5, 3]
max_profit = iterative(l)
print('first_solution:',max_profit)

p = iterative_no_list(l)
print('second_solution:',p)

