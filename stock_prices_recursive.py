def my_len_acc(l,acc_len=0):
	if not l:
		return acc_len
	return my_len_acc(l[1:],acc_len+1)

def my_len(l):
	if not l:
		return 0
	return 1+my_len(l[1:])

def my_max(l):
	if my_len_acc(l) == 1:
		return l[0]
	tail_max = my_max(l[1:])
	if l[0] > tail_max:
		return l[0]
	return tail_max

def stock(l):
	current_price = l[0]
	if my_len(l) == 1:
		return 0,current_price
	profit = my_max(l[1:]) - current_price
	return my_max([(profit,current_price),stock(l[1:])])

def buy_stock(l):
	profit, stock_price = stock(l)
	return stock_price

l = [9,11,8,16,5,10]
s = buy_stock(l)
print(s)
