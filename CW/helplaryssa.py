# help laryssa 

def leap (n):
    if n%400 == 0 or (n%4 ==0 and n%100):
        return True
    else:
        return False
    

def tri(n):
    for i in range (n):
        print ("*"*i)
    for i in range(n,0,-1):
        print("*"*i)



if __name__ == '__main__':
    tri(5)
    