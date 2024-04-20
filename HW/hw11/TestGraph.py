from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
       """initialize self.g so that it can be recalled for the tests"""
       Vs={'new york', 'houston', 'buffalo', 'cedar rapids', 'Philadelphia'}
       Es={('new york','houston', 1636), ('houston', 'buffalo', 1479), 
           ('buffalo', 'cedar rapids', 764), ('cedar rapids', 'Philadelphia', 989), 
           ('Philadelphia', 'new york', 97)}
       
       self.g = Graph(Vs, Es) # self.g available in all unittests
       # new york --------------- 97 mi --------------- philadelphia
       #   |                                                   |
       #   |                                                   |
       # 1636 mi                                             989 mi
       #   |                                                   |
       #   |                                                   |
       #   houston --- 1479 mi --- buffalo --- 764 mi --- cedar rapids

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    def test_addremove_vertices(self):
       """Tests that we can add and remove vertices from graph"""
       self.assertEqual(len(self.g), 5) # should have 5 vertices

       self.g.remove_vertex('new york')
       self.assertEqual(len(self.g), 4) # should have 4 vertices

       self.g.add_vertex('Denver')
       self.assertEqual(len(self.g), 5)
      
    def test_addremove_edges(self):
       """Tests that we can add and remove edges from graph"""
       # initally houston connects to buffalo
       n1 = {nbr for nbr in self.g.nbrs('houston')} #
       self.assertEqual(n1, {('buffalo', 1479)})

       # add connection from houston to philly
       self.g.add_edge('houston', 'Philadelphia', 2903)
       n1={nbr for nbr in self.g.nbrs('houston')}
       self.assertEqual(n1,{('buffalo', 1479), ('Philadelphia', 2903)})
      
       # remove connection from houston to buffalo
       self.g.remove_edge('houston', 'buffalo', 1479)
       n1 = {nbr for nbr in self.g.nbrs('houston')}
       self.assertEqual(n1, {('Philadelphia', 2903)})

    def test_iter(self):
       """Tests that iter goes over vertices correctly"""
       vs = {v for v in self.g}
       self.assertEqual(vs, {'new york', 'houston', 'buffalo', 'cedar rapids', 'Philadelphia'})

       self.g.add_vertex('Denver')
       vs = {v for v in self.g}
       self.assertEqual(vs,{'Denver', 'new york', 'houston', 'buffalo', 'cedar rapids', 'Philadelphia'})

       self.g.remove_vertex('new york')
       vs = {v for v in self.g}
       self.assertEqual(vs,{'houston', 'buffalo','Denver', 'cedar rapids', 'Philadelphia'})

class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
       """initialize self.g so that it can be recalled for the tests"""
       Vs={'new york', 'houston', 'buffalo', 'cedar rapids', 'Philadelphia'}
       Es={('new york', 'Philadelphia', 97),('new york', 'cedar rapids', 1024),('new york','houston', 1636), 
           ('houston', 'buffalo', 1479), ('buffalo', 'cedar rapids', 764), ('cedar rapids', 'Philadelphia', 989), 
           ('Philadelphia', 'new york', 97)}
       self.g = Graph(Vs, Es) # self.g available in all unittests

       # new york <--------------- 97 mi --------------> philadelphia
       #   |      ~~~~~~~~~~                                   ^
       #   |                ~~~~~~~~~~                         |
       # 1636 mi                    1024 mi                  989 mi
       #   |                          ~~~~~~~~~~               |
       #   V                                     ~~~~~~~~~>    |
       #   houston --- 1479 mi --> buffalo --- 764 mi --> cedar rapids
  
    # TODO: Which alg do you use here, and why?
    # Alg: bfs
    # Why: gives us the path with the fewest amount of edges, or number of trips
    def test_fewest_flights(self):
       """Tests that the tree returns the number of possible traversals minding paths already visited"""
       bfs_pairs=self.g.fewest_flights("new york")[-1]
       bfs_pairs_expected={'new york': 3, 'Philadelphia': 1, 'houston': 1, 'cedar rapids': 1, 'buffalo': 1}
       self.assertEqual(bfs_pairs, bfs_pairs_expected)

    # TODO: Which alg do you use here, and why?
    # Alg: dijkstra
    # Why: finds the shortest path while considering the weight of individual trips only
    def test_shortest_path(self):
       """Tests that the tree returns the distance of each city from the pivot city"""
       dij_pairs=self.g.shortest_path("new york")[-1]
       dij_pairs_expected={'new york': 0, 'houston': 1636, 'cedar rapids': 1024, 'Philadelphia': 97, 'buffalo': 3115}
       self.assertEqual(dij_pairs,dij_pairs_expected)

    # TODO: Which alg do you use here, and why?
    # Alg: prim
    # Why: gives us the shortest path while considering weight of entire trip
    def test_minimum_salt(self):
       """Tests that the tree returns the total distance"""
       prim_pairs=self.g.shortest_path("new york")[1]
       prim_pairs_expected={'new york': 0, 'houston': 1636, 'cedar rapids': 1024, 'Philadelphia': 97, 'buffalo': 3115}
       self.assertEqual(prim_pairs,prim_pairs_expected)

unittest.main()
