#letters.py

import string


def letter_count(file):
    '''takes a file as input and counts the amount each letter appears, counts capital and lowercase in the same catigory'''
    letterCount = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, 
                   "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

    file = open(file)

    for line in file:          
        line = line.lower() # changes all letters to lowercase for easier counting 
        for letter in line:

          if letter in letterCount:
            letterCount[letter] += 1 # increases letter count when that letter appears 

    file.close()
    
    return letterCount


def letter_frequency(dict):
    '''takes a file as input and calculates (using letter_count) the frequency of each letter in that file'''
    totalLetterCount = 0

    for item in dict.values():
        totalLetterCount += item # continually adds each individual letter count to total count 

    letterFreq ={} # create blank dictionary to be filled

    for key, value in dict.items():
        letterFreq [key] = float(value/totalLetterCount) # divides each individual letter count by the total letter count

    return letterFreq


#testing letter count, testing uses smaller sample size for easier manual checking
expectedcount = {"a":4, "b":3, "c":2, "d":1, "e":3, "f":2, "g":4, "h":5, "i":3, "j":6, "k":7, "l":1, "m":0, 
                 "n":3, "o":2, "p":1, "q":1, "r":3, "s":2, "t":4, "u":1, "v":2, "w":4, "x":3, "y":2, "z":6} #expected outcome 

actualcount = letter_count('empty_file.txt') # test trying to have the expected outcome

#print (actualcount)
#print (expectedcount)

assert (expectedcount == actualcount) # sees if the expected and the test are the same 

textcount = input("choose a file to count the amount of each letter ")
print(letter_count(textcount))


#testing letter frequency, testing uses smaller sample size for easier manual checking
testDict = {"a":2, "b":2, "c":2, "d":2, "e":2, "f":2, "g":2, "h":2, "i":2, "j":2, "k":2, "l":2, "m":0, 
            "n":2, "o":2, "p":2, "q":2, "r":2, "s":2, "t":2, "u":2, "v":2, "w":2, "x":2, "y":2, "z":2} #dictionary to be tested 

expectedoutcome = {'a': 0.04, 'b': 0.04, 'c': 0.04, 'd': 0.04, 'e': 0.04, 'f': 0.04, 'g': 0.04, 'h': 0.04, 'i': 0.04, 'j': 0.04, 'k': 0.04, 'l': 0.04, 'm': 0.0, 
                   'n': 0.04, 'o': 0.04, 'p': 0.04, 'q': 0.04, 'r': 0.04, 's': 0.04, 't': 0.04, 'u': 0.04, 'v': 0.04, 'w': 0.04, 'x': 0.04, 'y': 0.04, 'z': 0.04} #expected outcome 

test = letter_frequency(testDict) # test trying to have the expected outcome

#print(test)
#print(expectedoutcome)

assert (test == expectedoutcome) # sees if the expected and the test are the same 

textpercent = input("choose a file to get the freqeuncey of each letter ")
print(letter_frequency(letter_count(textpercent)))
