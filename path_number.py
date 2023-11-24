# Given a mxn grid a startung position at (0,0) and a target position (m,n)
# Find the total number of paths to reach the target knowing that we have
# Two possible moves: Go right or go down.

count_r = 0
count_m = 0
# Solution using recursion
def path_nb(m,n):
	global count_r
	count_r += 1

	if m == 1 and n == 1:
		return 1
	elif m == 1:
		return path_nb(1,n-1)
	elif n == 1:
		return path_nb(m-1,1)
	
	return path_nb(m-1,n)+path_nb(m,n-1)

# Solution using recursion with memoization
def path_nb_mem(m,n):
	global count_m
	count_m += 1

	if m == 1 and n == 1:
		return 1
	elif m == 1:
		return path_nb_mem(1,n-1)
	elif n == 1:
		return path_nb_mem(m-1,1)
	else:
		if mem[m-1][n] == 0:
			mem[m-1][n] = path_nb_mem(m-1,n)
		if mem[m][n-1] == 0:
			mem[m][n-1] = path_nb_mem(m,n-1)

	return mem[m-1][n]+mem[m][n-1]

def path_nb_it(m,n):
	for i_m in range(m):
		mem_itr[i_m][0] = 1
	for i_n in range(n):
		mem_itr[0][i_n] = 1
	for i in range(1,m):
		for j in range(1,n):
			mem_itr[i][j] = mem_itr[i-1][j]+mem_itr[i][j-1]
	return mem_itr[m-1][n-1]

m=5
n=5
mem = [[0]*(n+1) for __ in range(m+1)]
mem_itr = [[0]*(n) for __ in range(m)]
print('Total paths rec:', path_nb(m,n))
print('Nb of calls recursion',count_r)
print('Total paths rec+memo:',path_nb_mem(m,n))
print('NB of calls recursion + memo',count_m)
print('Total paths itr+memo:',path_nb_it(m,n))
