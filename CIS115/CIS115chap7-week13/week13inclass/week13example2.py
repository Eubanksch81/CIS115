##Charles Eubanks, week 13, Chapter 7
import random

def main():
    listNumbers = [0.0] * 5 ##[0,0,0,0,0]
    printList("at program start", listNumbers)
    
    modifyList(listNumbers)
    printList("after mod", listNumbers)
    
    listNumbers.append(random.randint(100,999)/10)
    printList("after append", listNumbers)

def modifyList(paramList):
    sizeOfList = len(paramList)
    for i in range(sizeOfList):
        paramList[i] = random.randint(100,999) / 10

def printList(paramStr, paramList):
    print(paramStr, "size =", len(paramList))
    
    for i in range(len(paramList)):
        if i % 4 == 0 and i > 0:
            print()
        print(paramList[i], end = "  ")

    for oneNumber in paramList:
        print(f"{oneNumber:.1f}", end = "   ")
    print()

    print()
   

main()
