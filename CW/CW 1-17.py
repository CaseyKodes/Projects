import random
MIN = 1
MAX = 16
num1 = random.randint(MIN,MAX)
attempts = 0
while True:
    while True:
        guess = input(f"Pick a number between {MIN} and {MAX} ")
        try:
            guess =int(guess)
            break
        except ValueError:
            print(f"Can not convert {guess} to int")
    if guess > MAX or guess < MIN:
        print ("your guess is not in the range try again")
        break
    if guess > num1:
        print("too high")
        attempts +=1
    elif guess < num1:
        print("too low")
        attempts +=1
    elif guess == num1:
        attempts +=1 
        print("nice job")
        print(f"You guessed the number in {attempts} attempts")
        break
    else:
        break 

    # python types 
    # ints 
    # floats 
    # bools 
    # python collections - can itterate over
    #   ordered collections - can index and slice
    # list - mutable 
    # strings 
    # tuples - not mutable 
    #   unordered collections - cannot index or slice
    # set
    # dictionaries 
    # 'is' = keyword checks memory location not value 