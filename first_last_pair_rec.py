def const(a,b):
	def pair(f):
		return f(a,b)
	return pair


def first_pair(a,b):
	print(a)

def second_pair(a,b):
	print(b)

def car(g):
	return g(first_pair)

def cdr(g):
	return g(second_pair)

car(const(3,4))
cdr(const(3,4))

