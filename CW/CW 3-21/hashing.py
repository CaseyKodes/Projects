# hashing
# and the mapping adt

# impliment mapping ADT

class Entry:
    def __init__(self, key, value):
        "Initializes a new entry w/ key and value"
        self.key = key
        self.value = value

    def __repr__(self):
        "String representation of entry"
        return f"Entry(key={self.key}, value={self.value})"

class ListMapping:
    def __init__(self):
        "Add data structure to store entries"
        self.L = []

    def __setitem__(self, k, v):
        "Add key:value pair to Mapping, or updated value if key already in mapping"
        newentry = Entry(k,v)
        for e in self.L:
            if e.key==k:
                e.value = v
                return 
        self.L.append(newentry)

    def __getitem__(self, k):
        "Return value associated with key. Raise a KeyError if key is not in mapping"
        for e in self.L:
            if e.key ==k:
                return e.value
        
        raise KeyError(f"key {k} is not in the list")

class hasmapping:
    def __init__(self):
        # create a list of empty lists 
        # why do you use a power of two easy division for computers since computer work in base two 
        nbuckets = 8

        self.L = [[] for i in range(self.nbuckets)]
        self.len = 0

    def __len__(self):
        return self.len
    
    def findbucket(self, key):
        return hash(key) % self.nbuckets
    
    def __setitem__(self, key, value):
        # find which bucket the key should be in 
        bucket = self.findbucket(key)    
        # scan that bucket update value if you find key
        for e in self.L[bucket]:
            if e.key == key:
                e.value = value
                return 
        # append empty bucket
        self.L[bucket].append(Entry(key, value))

        self.len +=1

        # rehash if too many items 
        if len(self) > self.nbuckets:
            self.rehash(2*self.nbuckets)

    def rehash(self, nbucketsnew):
        # create a new list of buckets 
        newL = [[] for i in range(nbucketsnew)]

        # rehash all existing entries 
        for bucket in self.L:
            for entry in bucket:
                newidx = self.findbucket(entry.key)
                newL[newidx] = entry
                
        # redirect self.L to the new list 
        self.L = newL
