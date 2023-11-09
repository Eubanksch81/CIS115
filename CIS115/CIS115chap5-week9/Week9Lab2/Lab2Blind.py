import random
def main():
    average1 = random.randint(55,100)
    average2 = random.randint(55,100)
    average3 = random.randint(55,100)
    ranAverage = randomAverage(average1, average2, average3)
    Grade = scoreFinder(ranAverage)

    printFunction("Grade 1", average1)
    printFunction("Grade 2", average2)
    printFunction("Grade 3 ", average3)
    printFunction("Average", ranAverage)
    print(Grade)

def randomAverage(p_average1, p_average2, p_average3):
    randomAverage = (p_average1 + p_average2 + p_average3) / 3
    return randomAverage

def scoreFinder(p_ranAverage):
    if p_ranAverage > 89:
        testGrade = "A"
    else: ##55 - 89.
        if p_ranAverage > 79: 
            testGrade = "B"
        else: ##55 - 79
            if p_ranAverage > 69:
                testGrade = "C"
            else:##55 - 69
                if p_ranAverage > 59:
                    testGrade = "D"
                else: ##55 - 59
                    testGrade = "F"
    return testGrade

def printFunction(param_str, param_int):
    print (f"{param_str}, {param_int:.1f}")

main()
