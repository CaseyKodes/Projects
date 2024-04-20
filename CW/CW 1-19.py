# 1/19 code 

'''
def foo ( arg1, arg2, agr3, arg4="hello", arg5="goodbye")
    return arg1, arg4

x = foo(1,2,3) # x = (1,"hello")
y,z = foo(1,2,3) # y = 1 z = "hello"
'''
'''

def uniqueStringBad(word):
    # inpout string 
    # output bool if every character in the string is unique 
    for item in word:
        if word.count(item) > 1: # inefficent 
            return False
    return True 

def uniqueStringGood(word):
    # inpout string 
    # output bool if every character in the string is unique 
    lword = len(word)
    lset = len(set(word))
    return lset == lword

def findFactors (list):
    # input a list of integers 
    # output a dictionary of integers 
    dict = {}
    for key in list:
        dict[key] = []
        for item in list:
            if key%item == 0:
                dict[key] += [item]
    return dict

test = [1,2,3,4,5,6,7,8,9,10]
print (findFactors(test))
'''

def uniqueStringMe(word):
    for item in word:
        newWord = word.replace(item,'',1)
        if item in newWord:
            return False 
    return True

print (uniqueStringMe("abc"))
print (uniqueStringMe("abb"))
