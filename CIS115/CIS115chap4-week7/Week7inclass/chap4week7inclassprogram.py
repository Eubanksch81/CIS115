##Charles Eubanks, Week 7, for loops 
##for loop statements are different in each language (c++, java, etc.)

##loop_cv = 0
##while loop_cv < 4:
##    print (f"{loop_cv} hello", end = "\t\t")
##    loop_cv += 1
##print (f"\n-----------------")

##                  start value (all for CISmajor)
##                      < this value (upto but not including)
##                          increment
for loop_cv in range(0, 4, 1): ##loop_cv must be an int, and must be < this number.
    ##for statement removes the need for loop_cv = 0 from line 4
    ##since loop_cv is set automatically.
    print (f"{loop_cv}", end = "\t\t")
    ##also, loop_cv is automatically incremented by 1 at the bottom of the loop.
    
print (f"\n--------------------------------------")

##for(loop_cv) = 0; loop_cv < 4; loop_cv += 1)
##Other languages' for statements. Try to use this instead.

##printing 2,4,6,8,10,12,14
for loop2_cv in range(2,15,2):
    print (f"{loop2_cv}", end = "\t\t")

##nested loops.
    total_score = 0
for test_num in range(0,3,1): ##Gets 3 different test_score variables.
    test_score = int(input(f"\nEnter test score: "))
    total_score += test_score

##Adds up all test_score variables into one variable.
avg_score = total_score/3 ##Divides by num of variables for average.
print(f"Average - {avg_score:.1f}") ##Prints average.
