##Charles Eubanks, week 13, Chapter 7
import random

def main():
    lstNumbers = [0] * 5 ##[0,0,0,0,0]
    printList("at program start", lstNumbers)
    modifyList(lstNumbers)
    printList("after mod", lstNumbers)

def modifyList(paramLst):
    sizeOfList = len(paramLst)
    for i in range(sizeOfList): ##sizeOfList = 5. i takes up values 0,1,2,3,4
        paramLst[i] = random.randint(100,999) / 10

def printList(paramStr, paramLst):
    sizeOfList = len(paramLst)
    print(f"{paramStr}, size = {sizeOfList}")

    for oneNumber in paramLst:
        print(f"{oneNumber:.1f}", end = "   ")
    print()
    

main()
