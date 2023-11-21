def wrap_subset_sum(l,target):
	if target == 0:
		return ([],True)
	if target < 0 or len(l) == 0:
		return ([],False)
	
	t_sub = wrap_subset_sum(l[1:],target-l[0])
	do_take, val_do = [l[0]]+t_sub[0],t_sub[1]
	no_take, val_no = wrap_subset_sum(l[1:],target)
	
	if val_do == True:
		return do_take, True
	elif val_no == True:
		return no_take, True
	else:
		return [],False

def subset_sum(l,t):
	l_res, t_res = wrap_subset_sum(l,t)
	return l_res

l = [12,1,61,5,9,2]
t = 24
print(subset_sum(l,t))
