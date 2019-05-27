from random import randint
from time import time
from sys import argv

'''

Make a list length of highest number
add one to the index of a number each time the number is seen
go through the list and make a new list using the number at each index

'''

#------------------------------------------------------------------------------
#removes extra numbers
def makeUnique(inList):
    midList = [0] * 101
    outList = list()
    for num in inList:
        midList[num] += 1

    numA = 0
    for x in midList:
        for y in range(x):
            outList.append(numA)
        numA += 1
    return outList

#------------------------------------------------------------------------------
#main function
def main():
    length = 10  # Default list length
    if (len(argv) >= 2):
        length = int(argv[1])
        print("Building a {}-element list.".format(length))
    else:
        print("No length specified. Building a 10-element list.")
    numList = [randint(0, 100) for i in range(length)]

    print(makeUnique(numList))

main()
