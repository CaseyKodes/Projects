# BSTMap

from BSTNode import BSTNode

class BSTMap:
    def __init__(self):
        """Creates a new BSTMap"""

    def put(self, key, value):
        """adds k:v pair to BSTMap"""

    def get(self, key):
        """Returns value associated w/ key"""

    def __contains__(self, key):
        """Returns true if key is in BSTMap, false otherwise"""

    def __repr__(self):
        """Returns string representation of BSTMap"""

if __name__ == '__main__':
     
    bst1 = BSTMap()
    for i in range(8):
        assert not i in bst1        # test contains (false)
        bst1.put(i, str(i))
        assert bst1.get(i) == str(i)    # tests put/get 
        assert i in bst1            # tests contains (true)

    print(bst1)