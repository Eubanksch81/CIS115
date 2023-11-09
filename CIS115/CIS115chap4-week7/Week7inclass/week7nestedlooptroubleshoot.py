##nested loops.
total_score = 0
for test_num in range(0,3,1): ##Gets 3 different test_score variables.
    test_score = int(input(f"\nEnter test score: "))
    while test_score < 0 or test_score > 100:
        print(f"Invalid score!")
        test_score = int(input(f"Enter test score."))
        
    total_score += test_score


total_score += test_score ##Adds up all test_score variables into one variable.
avg_score = total_score/3 ##Divides by num of variables for average.
print(f"Average - {avg_score:.1f}") ##Prints average.
