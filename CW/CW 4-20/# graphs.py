# graphs 

# graph traversal algorithms 
'''

using ajacentcy set 
explore one path add the next steps created after the first step but keep all other first possible steps 
    repeat 
    try not to vist a vertex more than once 
        sounds recursive 
dictionary of child parent pairs 
    stores tree as a dictionary that can be traveres easier 

'''

def traverse(start):
    '''
    you can either run a traversal algorithm with a queue or a stack but a queue is more highly optimized
    '''

    # initialize 
    # 1 make empty collection of to_vist and tree
    # 2 add (start, none) to to_visit 

    # traverse 
    # 3 until to_visit is empty:
        # 3a child, parent = to_visit_remove()
        # 3b add child, parent to tree
        # 3c add childs neighbors to to_visit

    # return 
    # 4 return tree
    pass

'''
dijkstra finds the minimum wight of each path connecting the start to everything else

'''
