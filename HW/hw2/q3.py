from pathlib import Path
import time

# binary search algorithm 
def binarySearch(array, target):
    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1

# brute force method 
def sum2IntBrute(target, list):
        for i in range(len(list)):
            for j in range(i, len(list)):
                if (list[i] + list[j] == target):
                    string = f"{target} is equal to {list[i]} + {list[j]}."
                    return string 
        return f"{target} can not be expressed as the sum of two numbers in the list."

# sum2 but uses binary search to be faster
def sum2IntFast(target, list):
    list.sort()
    for i in range(len(list)):
        secondHalf = target - list[i]
        found = binarySearch(list, secondHalf)
        if found != -1:
            string = f"{target} is equal to {list[i]} + {list[found]}."
            return string
    return f"{target} can not be expressed as the sum of two numbers in the list."
    

if __name__ == '__main__': 

    # all files are accesable 
    dataFolder = Path("C:/Users/casey/OneDrive/Desktop/Spring 2024/CSE 3500/HW/hw2/CollectionNumbers")
    # all files with lists of numbers

    # code to make list of values useable 
    listnum10 = open(dataFolder / "listNumbers-10.txt")
    values10 = []
    for line in listnum10:
        values10.append(int(line.strip()))

    listnum100 = open(dataFolder / "listNumbers-100.txt")
    values100 = []
    for line in listnum100:
        values100.append(int(line.strip()))

    listnum1000 = open(dataFolder / "listNumbers-1000.txt")
    values1000 = []
    for line in listnum1000:
        values1000.append(int(line.strip()))

    listnum10000 = open(dataFolder / "listNumbers-10000.txt")
    values10000 = []
    for line in listnum10000:
        values10000.append(int(line.strip()))

    listnum100000 = open(dataFolder / "listNumbers-100000.txt")
    values100000 = []
    for line in listnum100000:
        values100000.append(int(line.strip()))

    listnum1000000 = open(dataFolder / "listNumbers-1000000.txt")
    values1000000 = []
    for line in listnum1000000:
        values1000000.append(int(line.strip()))

    # all files with lists of sums to search for (nsol)
    nsol10 = open(dataFolder / "listNumbers-10-nsol.txt")
    nsol100 = open(dataFolder / "listNumbers-100-nsol.txt")
    nsol1000 = open(dataFolder / "listNumbers-1000-nsol.txt")
    nsol10000 = open(dataFolder / "listNumbers-10000-nsol.txt")
    nsol100000 = open(dataFolder / "listNumbers-100000-nsol.txt")
    nsol1000000 = open(dataFolder / "listNumbers-1000000-nsol.txt")

    print("\n\nUsing the brute force method\n")

    print("\nlistNumbers-10 Brute")
    total10 = 0
    for line in nsol10:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values10))
        end = time.time() 
        total10 += (end-start)
    average10 = total10/10
    print(f"Average running time for listNumbers-10 was {average10}")

    print("\nlistNumbers-100 Brute")
    total100 = 0
    for line in nsol100:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values100))
        end = time.time()
        total100 += (end-start)
    average100 = total100/10
    print(f"Average running time for listNumbers-100 was {average100}")

    print("\nlistNumbers-1000 Brute")
    total1000 = 0
    for line in nsol1000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values1000))
        end = time.time()
        total1000 += (end-start)
    average1000 = total1000/10
    print(f"Average running time for listNumbers-1000 was {average1000}")

    print("\nlistNumbers-10000 Brute")
    total10000 = 0 
    for line in nsol10000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values10000))
        end = time.time()
        total10000 += (end-start)
    average10000 = total10000/10
    print(f"Average running time for listNumbers-10000 was {average10000}")

    print("\nlistNumbers-100000 Brute")
    total100000 = 0
    for line in nsol100000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values100000))
        end = time.time()
        total100000 += (end-start)
    average100000 = total100000/10
    print(f"Average running time for listNumbers-100000 was {average100000}")

    print("\nlistNumbers-1000000 Brute")
    total1000000 = 0
    for line in nsol1000000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntBrute(int(use), values1000000))
        end = time.time()
        total1000000 += (end-start)
    average1000000 = total1000000/10
    print(f"Average running time for listNumbers-1000000 was {average1000000}")

    # code to make list of values useable 
    listnum10 = open(dataFolder / "listNumbers-10.txt")
    values10 = []
    for line in listnum10:
        values10.append(int(line.strip()))

    listnum100 = open(dataFolder / "listNumbers-100.txt")
    values100 = []
    for line in listnum100:
        values100.append(int(line.strip()))

    listnum1000 = open(dataFolder / "listNumbers-1000.txt")
    values1000 = []
    for line in listnum1000:
        values1000.append(int(line.strip()))

    listnum10000 = open(dataFolder / "listNumbers-10000.txt")
    values10000 = []
    for line in listnum10000:
        values10000.append(int(line.strip()))

    listnum100000 = open(dataFolder / "listNumbers-100000.txt")
    values100000 = []
    for line in listnum100000:
        values100000.append(int(line.strip()))

    listnum1000000 = open(dataFolder / "listNumbers-1000000.txt")
    values1000000 = []
    for line in listnum1000000:
        values1000000.append(int(line.strip()))

    # all files with lists of sums to search for (nsol)
    nsol10 = open(dataFolder / "listNumbers-10-nsol.txt")
    nsol100 = open(dataFolder / "listNumbers-100-nsol.txt")
    nsol1000 = open(dataFolder / "listNumbers-1000-nsol.txt")
    nsol10000 = open(dataFolder / "listNumbers-10000-nsol.txt")
    nsol100000 = open(dataFolder / "listNumbers-100000-nsol.txt")
    nsol1000000 = open(dataFolder / "listNumbers-1000000-nsol.txt")

    print("\n\nNow using the faster method\n")

    print("\nlistNumbers-10 Fast")
    total10 = 0
    for line in nsol10:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values10))
        end = time.time() 
        total10 += (end-start)
    average10 = total10/10
    print(f"Average running time for listNumbers-10 was {average10}")

    print("\nlistNumbers-100 Fast")
    total100 = 0
    for line in nsol100:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values100))
        end = time.time()
        total100 += (end-start)
    average100 = total100/10
    print(f"Average running time for listNumbers-100 was {average100}")

    print("\nlistNumbers-1000 Fast")
    total1000 = 0
    for line in nsol1000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values1000))
        end = time.time()
        total1000 += (end-start)
    average1000 = total1000/10
    print(f"Average running time for listNumbers-1000 was {average1000}")

    print("\nlistNumbers-10000 Fast")
    total10000 = 0 
    for line in nsol10000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values10000))
        end = time.time()
        total10000 += (end-start)
    average10000 = total10000/10
    print(f"Average running time for listNumbers-10000 was {average10000}")

    print("\nlistNumbers-100000 Fast")
    total100000 = 0
    for line in nsol100000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values100000))
        end = time.time()
        total100000 += (end-start)
    average100000 = total100000/10
    print(f"Average running time for listNumbers-100000 was {average100000}")

    print("\nlistNumbers-1000000 Fast")
    total1000000 = 0
    for line in nsol1000000:
        i = 0
        use = ""
        while (line[i] != '\n'):
            use += line[i]
            i += 1
        start = time.time()
        print(sum2IntFast(int(use), values1000000))
        end = time.time()
        total1000000 += (end-start)
    average1000000 = total1000000/10
    print(f"Average running time for listNumbers-1000000 was {average1000000}")