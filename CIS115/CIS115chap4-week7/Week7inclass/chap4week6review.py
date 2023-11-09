##Charles Eubanks, Week 6, Chapter 4
##Loop structures
##Two types of loops; pre-test loops, and post-test loops.
##Pre-test Loop statements come from if questions,
##If true/false, perform actions and repeat. minimum iterations = 0
##post-test loops arent implemented into python. minimum interations = 1
##post-test loops repeat back to original statements, not the if statement.
##also condition controlled "while" loops, counter controlled "for" loops
##Infinite loops will never be used.

loop_cv = 0 ##Use 0 to get the same amount of loop statements as the
##boolean number.

while loop_cv < 8:
    if loop_cv % 4 == 0: ##Keeps 4 statements on one line.
        print()
    print (f"Hello! {loop_cv}", end = "\t")
    loop_cv = loop_cv + 1 ##Goes back to line 13.
    ##Loop statements require a loop control variable, other loop is infinite.

print (f"\nloop has ended.")

test_score = int(input(f"Enter your test score from 0-100. "))

while test_score < 0 or test_score > 100: ##Date is invalid, "bad".
    print(f"Invalid! Must be 0-100!")
    test_score = int(input(f"Enter your test score from 0-100. "))

print (f"Data entry successful. Nice.")
##test_score < 0 bad
##test_score > 100 bad
##test_score > -1 good
##test_score < 101 good
##For ctrlc

num_attempts = 1 ##For future use on number of attempts.
##print (f"Attempt # {num_attempts}")
user_pw = input(f"Enter password.")
corr_pw = "wcc2021"

while user_pw != corr_pw:
    num_attempts += 1 ##Increases num_attempts by 1.
    print(f"Attempt # {num_attempts}")
    user_pw = input(f"Incorrect. Enter password.")
    if num_attempts > 2: ##Only 3 attempts, meaning can only misinput twice.
        print (f"Login failed. Try again later.")
        quit() ##If login fails 3 times, kills program.
print (f"Login successful.")

##while user_pw != corr_pw and num_attempts <= 4:
##    num_attempts += 1
##    print (f"Attempt # {num_attempts}")
##    user_pw = input(f"Invalid! Enter password: ")
##
##if user_pw == corr_pw:
##    print (f"Login successful.")
##else:
##    print (f"Login failed.")
##Mrs. Tolappas' version.
