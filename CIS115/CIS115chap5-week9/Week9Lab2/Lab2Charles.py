##Charles Eubanks CIS950, Mrs. Tolappa, Lab 2

import random
def main():  ##Gets 3 random ints, gets average, grades average, prints.
    average1 = random.randint(55,100)
    average2 = random.randint(55,100)
    average3 = random.randint(55,100)
    ranAverage = getAverage(average1, average2, average3)
    ranGrade = getGrade(ranAverage)

    printScores("Score 1", average1)
    printScores("Score 2", average2)
    printScores("Score 3", average3)
    printScores(f"Score average",ranAverage)
    print(f"Grade = {ranGrade}")

def getAverage(p_average1, p_average2, p_average3):
    randomAverage = int(p_average1 + p_average2 + p_average3) / 3
    return randomAverage

def getGrade(p_randomAverage):
    if p_randomAverage > 89:
        testGrade = "A"
    else: ##55 - 89.
        if p_randomAverage > 79: 
            testGrade = "B"
        else: ##55 - 79
            if p_randomAverage > 69:
                testGrade = "C"
            else:##55 - 69
                if p_randomAverage > 59:
                    testGrade = "D"
                else: ##55 - 59
                    testGrade = "F"
    return testGrade
    
def printScores(p_avg_str,p_avg_int):
    print(f"{p_avg_str} is {p_avg_int:.1f}")


main()

##Sample Output
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap5-week9\Week9Lab2\Lab2Charles.py
##Score 1 is 71.0
##Score 2 is 78.0
##Score 3 is 56.0
##Score average is 68.3
##Grade = D
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap5-week9\Week9Lab2\Lab2Charles.py
##Score 1 is 95.0
##Score 2 is 83.0
##Score 3 is 98.0
##Score average is 92.0
##Grade = A
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap5-week9\Week9Lab2\Lab2Charles.py
##Score 1 is 63.0
##Score 2 is 74.0
##Score 3 is 73.0
##Score average is 70.0
##Grade = C
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap5-week9\Week9Lab2\Lab2Charles.py
##Score 1 is 63.0
##Score 2 is 82.0
##Score 3 is 64.0
##Score average is 69.7
##Grade = C
##>>> 
