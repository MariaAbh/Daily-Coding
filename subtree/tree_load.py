class Tree:
    __slots__ = ['value', 'left', 'right']
    def __init__(self, v, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right
    def __eq__(self, other):
        return (
            other and
            self.value == other.value and
            self.right == other.right and
            self.left == other.left
        )

def stutter(it):
    for v in it:
        yield v,0
        yield v,1

def load_tree(levels):
    if not levels:
        return None
    first, *levels = levels
    if not (len(first) == 1 and first[0] is not None):
        return None

    current = [Tree(v) for v in first]
    root = current[0]
    for lvl in levels:
        next_level = []
        for (parent,id), value in zip(stutter(current), lvl):
            if value is None: continue
            child = Tree(value)
            if id:
                parent.right = child
            else:
                parent.left = child
            next_level.append(child)
        current = next_level
    return root


L = None
tree = load_tree([
    [              0            ],
    [        1     ,     2      ],
    [     3  ,  4  ,  5  ,  6   ],
    [    L,L , L,7 , 8,9 , L,L  ],
])

# yeah = tree == Tree(
#     0,
#     Tree(
#         1,
#         Tree(3),
#         Tree(
#             4,
#             right=Tree(7)
#         ),
#     ),
#     Tree(
#         2,
#         Tree(
#             5,
#             Tree(8),
#             Tree(9),
#         ),
#         Tree(6),
#     ),
# )
# print(yeah)
