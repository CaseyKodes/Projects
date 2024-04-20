# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = 1000 # Max is 2000 due to memory constraints with quicksort
u = [random.randint(0, n) for i in range(n)]
s = [i for i in range(1000)]
r = [i for i in range(1000,0,-1)]

##### Create file to write to #####
f = open(f"./numbers.txt", "w")

##### Write numbers to file #####
for item in s:
    f.write(str(item))
    f.write(" ")

#### Close the file ####
f.close()


