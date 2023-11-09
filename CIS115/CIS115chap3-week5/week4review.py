##CIS115.950, week 4 review

import random
##Imports a stored library that runs a random number.Period shows libraries
stu_points = random.randint(50,100)
print(f"stu_points = {stu_points}")
##Example1
if stu_points>= 90:
    print (f"A! Fantastic!")
else: ##55-89.
    if stu_points >= 80: 
        print(f"B! Good job!")
    else: ##55-79
        if stu_points >= 70:
            print(f"C! Just a little bit more!")
        else:
            if stu_points >= 60:
                print (f"D! Barely made it.")
            else:
                print(f"F! Better luck next time.")
## Most efficient way to code these statements, but is hard to understand.
##Example2
if stu_points >= 90:
    print (f"--A--")

if stu_points >= 80 and stu_points <= 89:
    print(f"--B--")

if stu_points >= 70 and stu_points <=79:
    print(f"--C--")

if stu_points >= 60 and stu_points <= 69:
    print (f"--D--")

if stu_points < 60:
    print (f"--F--")
##Another way to code the same statement; easier to understand.
##Example3
if stu_points >= 90:
    print (f"A")
elif stu_points >= 80:
    print (f"B")
elif stu_points >= 70:
    print (f"C")
elif stu_points >= 60:
    print (f"D")
else
    print(f"F")
##Recommended to do Example 1 as a CIS major. elif is "else if".
##CS majors will have to do >89 instead of >= 90 as it is more efficient.
