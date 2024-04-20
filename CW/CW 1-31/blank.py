# blank.py

import time

def timef(func, arg):
    'returns the time to run a function'
    start = time.time()
    func(arg)
    end = time.time()
    return end-start

def clista(n):
    L= []
    for i in range(n):
        L.append(i+1)
    return L

def clistb(n):
    L=[]                        
    for i in range(n):          
        L.insert(0, n-i)    
    return L                

if __name__ == '__main__':
    # table header
    print('='*40)
    x = 'n'
    y = 't_a (ms)'
    z = 't_b (ms)'
    print(f"{x:<10}{y:<10}{z:<10}")
    print('-'*40)

    for n in [1000,2000,5000,10000]:
        t_a = 1000*timef(clista, n)
        t_b = 1000*timef(clistb, n)

        print (f"{n:<10}{t_a:<10.3f}{t_b:<10.3f}")
    