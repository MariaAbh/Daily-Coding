class Node():
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

def sum_trees(tree1,tree2):
	if tree1 == None and tree2 == None:
		return None

	if tree1 == None:
		new_node = Node(tree2.value)
		new_node.left = sum_trees(None,tree2.left)
		new_node.right = sum_trees(None,tree2.right)
		return new_node
	elif tree2 == None:
		new_node = Node(tree1.value)
		new_node.left = sum_trees(tree1.left,None)
		new_node.right = sum_trees(tree1.right,None)
		return new_node

	new_node = Node(tree1.value + tree2.value)
	new_node.left = sum_trees(tree1.left,tree2.left)
	new_node.right = sum_trees(tree1.right,tree2.right)
	return new_node

def tree_p(tree):
	if tree == None:
		return []
	else:
		nodes = [f'{str(tree.value)}']
		tree_l = tree_p(tree.left)
		tree_r = tree_p(tree.right)
		if not tree_l:
			left = []
		else:
			left = ['├─'+tree_l[0]]+['│ '+s for s in tree_l[1:]]
		if not tree_r:
			right = []
		else:
			right = ['└─'+tree_r[0]]+['  '+s for s in tree_r[1:]]
		return nodes + left + right

def print_tree_p(l):
	for e in l:
		print(e)

def main():
	Tree1 = Node(5)
	Tree1.right = Node(10)
	Tree1.left = Node(15)
	Tree1.left.left = Node(30)
	Tree1.left.right = Node(40)
	Tree1.right.left = Node(11)
	Tree2 = Node(3)
	Tree2.right = Node(9)
	Tree2.left = Node(6)
	
	print('First tree:')
	t1 = tree_p(Tree1)
	print_tree_p(t1)
	print('\nSecond tree:')
	t2 = tree_p(Tree2)
	print_tree_p(t2)

	new_tree = sum_trees(Tree1,Tree2)
	print('\nTrees sum:')
	t3 = tree_p(new_tree)
	print_tree_p(t3)

main()
