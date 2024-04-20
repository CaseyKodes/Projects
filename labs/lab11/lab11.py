# lab 11

class Graph_AS: # adjusanty set
    def __init__(self, V = (), E = ()):
        self.V = set()
        self.nbrs = dict()
        for v in V: self.add_vertex(v)
        for a, b in E: self.add_edge((a, b))
    
    def __len__(self):
        return len(self.V)
    
    def add_vertex(self, v):
        self.V.add(v)

    def remove_vertex(self, v):
        self.V.remove(v)

    def add_edge(self, e):
        k, v = e
        if k not in self.nbrs:
            self.nbrs[k] = {v}
        else:
            self.nbrs[k].add(v)
    
    def remove_edge(self, e):
        k, v = e
        self.nbrs[k].remove(v)
        if len(self.nbrs[k]) == 0:
            self.nbrs.pop(k)

    def __iter__(self):
        return iter(self.V)

    def _neighbors(self, v):
        return iter(self.nbrs[v])
    

class Graph_ES: # edge set
    def __init__(self, v, e):
        self.V = v
        self.E = e
    
    def __len__(self):
        return len(self.V)

    def add_edge(self, e):
        self.E.add(e)
    
    def add_vertex(self, v):
        self.V.add(v)

    def remove_edge(self, e):
        self.E.remove(e)

    def remove_vertex(self, v):
        self.V.remove(v)

    def __iter__(self):
        return iter(self.V)
    
    def _neighbors(self, v):
        neighbors = set()
        for edge in self.E:
            if edge[0] == v:
                neighbors.add(edge[1])
        return neighbors
    
