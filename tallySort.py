from random import randint
from sys import argv

#------------------------------------------------------------------------------
#check for item in list
def checkList(x, unique):
    for y in unique:
        if x == y:
            return False
    return True

#------------------------------------------------------------------------------
#function for expanding a list
def expandList(value):
    exList = []
    for i, x in enumerate(value):
        for j in range(x):
            exList.append(i)
    return exList

#------------------------------------------------------------------------------
#reduces the list to unique numbers
def listOptimization(listOrigin):
    listUnique = list()
    highest = max(listOrigin)
    counts = [0 for x in range(highest + 1)]

    for x in listOrigin:
        counts[x] += 1
        if checkList(x, listUnique):
            listUnique.append(x)
    return counts

#------------------------------------------------------------------------------
#main function
def main():
    length = 10  # Default list length
    if (len(argv) >= 2):
        length = int(argv[1])
        print("Building a {}-element list.".format(length))
    else:
        print("No length specified. Building a 10-element list.")

    # Create random array using list comprehension
    if length >= 100:
        array = [randint(0, round(length*0.1)) for i in range(length)]
    else:
        array = [randint(0, 10) for i in range(length)]
    tally = listOptimization(array)
    tally = expandList(tally)

    print(tally)

main()
