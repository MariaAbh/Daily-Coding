#56 Given undirected graph and k colors, determine if each node in graph can be colored such that #     no 2 adjacent vertices have the same color.

def is_colorable(graph,k):
    for row in graph:
        if sum(row) == k:
            return False
    return True

graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,0],
        [1,0,0,0]
]
k = 3
print(is_colorable(graph,k))
