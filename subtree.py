# 1619
# check whether tree t has exactly the same structure and node values with a subtree of tree s

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def contains_subtree(t,s):
    if t == None and s == None:
        return True
    if t == None or s == None:
        return False

    if t.value == s.value:
        return contains_subtree(t.left,s.left) and contains_subtree(t.right,s.right)
    else:
        return contains_subtree(t.left,s) or contains_subtree(t.right,s) or contains_subtree(t,s.left) or contains_subtree(t,s.right)

if __name__ == "__main__":
    t = Node(4,Node(5,Node(1,Node(2),Node(3)),Node(10)),Node(6))
    s1 = Node(1,Node(2),Node(3))
    print(contains_subtree(t,s1))
    s2 = Node(111)
    print(contains_subtree(t,s2))
    s3 = Node(2)
    print(contains_subtree(t,s3))

