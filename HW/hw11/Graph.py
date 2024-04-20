class Graph:
   def __init__(self, V=(), E=()):
       """creates a graph with vertex and edge sets"""
       self.V = set()
       self.E = dict()
       for v in V: self.add_vertex(v)
       for u,v,wt in E: self.add_edge(u,v,wt)

   def __len__(self):
       return len(self.V)

   def __iter__(self):
       return iter(self.V)

   def add_vertex(self, v):
       """adds vertex to graph"""
       self.V.add(v)

   def remove_vertex(self, v):
       """removes vertex from graph"""
       if v not in self.V: raise KeyError
       else: self.V.remove(v)

   def add_edge(self, u, v, wt):
       """adds edge to graph"""
       if u not in self.E: self.E[u]= {(v,wt)}
       else:
           self.E[u].add((v,wt))

   def remove_edge(self, u, v, wt):
       """removes edge from graph"""
       if (v,wt) not in self.E[u]: raise KeyError
       else:
           self.E[u].remove((v,wt))
           if len(self.E[u])==0: self.E.pop(u)

   def nbrs(self, v):
       """returns an iterator over neighbors of v"""
       return iter(self.E[v])
  
   def fewest_flights(self, city):
       # tree and dist are distcint dictionaries to be read and add to and from during the finding of the path

       tree={} 
       dist={} 
       tovisit=[(None,city)]

       while tovisit:
           a,b=tovisit.pop(0)
           if b not in tree:
               # adds a value you tree the first time it is seen in tovisit
               counter=0
               tree[b]=a
               for n,wt in self.nbrs(b):
                   # adds the neighbors of the current spot to to visit
                   tovisit.append((b,n))
                   counter+=1
               dist[b]=counter

       return tree, dist 

   def shortest_path(self,city):
       # tree and dist are distcint dictionaries to be read and add to and from during the finding of the path

       tree={} 
       dist={city: 0} 
       tovisit=[(None,city)]

       while tovisit:
           dist[city]=0
           a,b=tovisit.pop(0)       
           if b not in tree:
            # adds a value you tree the first time it is seen in tovisit

               tree[b]=a
               for n,wt in self.nbrs(b):
                   # adds the neighbors of the current spot to to visit

                   tovisit.append((b,n))
                   tovisit.sort(reverse=True)
                  
               if a==city:
                   for n,wt in self.nbrs(a):
                       # if we are at the original city we have found our path
                       if b == n: dist[b]=wt

               else:
                   if a in tree:
                       for n,wt in self.nbrs(a):
                        # adds the neighbors of the current spot to to visit

                           dist[b]= dist[a]+wt           

       return tree,dist 
      
   def minimum_salt(self,city):
       # tree and dist are distcint dictionaries to be read and add to and from during the finding of the path
       tree={} 
       dist={} 
       tovisit=[(None,city)]
       counter=0 # keeping tracking total mileage
      
       while tovisit:
           a,b=tovisit.pop()
           if b not in tree:
               tree[b]=a
               dist[b]=counter # assigning vertex : pair
               maxcounter=0 
               for n,wt in self.nbrs(b):
                   tovisit.append((b,n))
                   tovisit.sort(reverse=True)
                   if wt>maxcounter: maxcounter=wt
               counter+=maxcounter # adding miles to total travel
              
       return tree, dist 
   
