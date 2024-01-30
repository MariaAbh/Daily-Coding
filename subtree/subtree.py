import tree_load as tl

def is_subtree(s,t):
    if is_equal(t,s):
        return True
    if s == None:
        return False
    return is_subtree(s.left,t) or is_subtree(s.right,t)


def is_equal(t,s):
    if t == None and s == None:
        return True
    if t == None or s == None:
        return False
    if t.value != s.value:
        return False
    return is_equal(t.right,s.right) and is_equal(t.left,s.left)

L = None
s = tl.load_tree([
    [              0            ],
    [        1     ,     2      ],
    [     3  ,  4  ,  5  ,  6   ],
    [    L,L , L,7 , 8,9 , L,L  ],
])

t = tl.load_tree([
    [ 4 ],
    [L,7],
])

print(is_subtree(s,t), True)

s = tl.load_tree([
    [              0            ],
    [        1     ,     2      ],
    [     3  ,  4  ,  5  ,  6   ],
    [    L,L , L,7 , 8,9 , L,L  ],
])

t = tl.load_tree([
    [ 4 ],
    [5,7],
])

print(is_subtree(s,t), False)

s = tl.load_tree([
    [              0            ],
    [        1     ,     2      ],
    [     3  ,  4  ,  5  ,  6   ],
    [    L,L , L,7 , 8,9 , L,L  ],
])

t = tl.load_tree([
    [    1  ],
    [ 3  ,  4],
    [L,L , L,7],
])

print(is_subtree(s,t), True)



s = tl.load_tree([
    [              0            ],
    [        1     ,     2      ],
    [     3  ,  4  ,  5  ,  6   ],
    [    L,L , L,7 , 8,9 , L,L  ],
])

t = tl.load_tree([
    [    0  ],
    [ 3  ,  6],
    [L,L , L,L],
])

print(is_subtree(s,t), False)
