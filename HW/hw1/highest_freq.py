# highest_freq.py

import letters

# takes a file as input and calculates the letter that appears the most in that file
def highest_freq(file):

    maxpercent = -1 # initializes maxpercent at -1 percent, holds the percent that the most highly occuring letter occured at as a decimal between 0 and 1 
                    # -1 percent is used since it will never occur so maxpercent will alwyas get written over

    maxkey = " " # creates a blank max key which holds the actual letter that has the most occurences, initially blank to be written over 

    data = letters.letter_frequency(letters.letter_count(file)) # creates new dictionary to avoid unwanted editing of roiginal dictionary

    for key, value in  data.items(): # loops through data 

        if value > maxpercent: # tests max value and if new max is found changes the values to new found max values 
            maxpercent = value
            maxkey = key


    tuple = (maxkey, maxpercent)

    return tuple 


#testing highest freq, testing uses smaller sample size for easier manual checking
expectedoutcome = ('a', .5) # expected outsome 

testoutcome = highest_freq('test_for_highest.txt') # test trying to have expected outcome 

#print (expectedoutcome)
#print (testoutcome)

assert (expectedoutcome == testoutcome) # sees if the test and the expected are the same 

highfreq = input("choose a file to find the most prevelant letter in ")
print (highest_freq(highfreq))
