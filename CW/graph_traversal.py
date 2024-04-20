# graph_traversal




# only difference between bfs and ds is bsf uses a queue and dfs uses a stack

def dfs(self, v):
    # uses a stack
    tree = {}
    tovisit = [(None, v)]
    while tovisit:
        a,b = tovisit.pop()
        if b not in tree:
            tree[b] = a
            for n in self.nbrs(b):
                tovisit.append((b,n))
    return tree

def bfs(G, v):
    # uses a queue
    tree = {}
    tovisit = Queue()
    tovisit.enqueue((None, v))
    while tovisit:
        a,b = tovisit.dequeue()
        if b not in tree:
            tree[b] = a
            for n in G.nbrs(b):
                tovisit.enqueue((b,n))
    return tree


# difference between dijkstra and prim, 
#   dijkstra finds the minium path from a start to an end node/vertex
#   prim finds the minimum spanning tree

def dijkstra(G, v):
    tree = {}
    D = {v: 0}
    tovisit = PriorityQueue()
    tovisit.insert((None,v), 0)
    for a,b in tovisit:
        if b not in tree:
            tree[b] = a
            if a is not None:
                D[b] = D[a] + G.wt(a,b)
            for n in G.nbrs(b):
                tovisit.insert((b,n), D[b] + G.wt(b,n))
    return tree, D

def prim(G):
    v = next(iter(G.vertices()))
    tree = {}
    tovisit = PriorityQueue()
    tovisit.insert((None, v), 0)
    for a, b in tovisit:
        if b not in tree:
            tree[b] = a
            for n in G.nbrs(b):
                tovisit.insert((b,n), G.wt(b,n))
    return tree
