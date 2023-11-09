##Week 4,Program 2; Charles Eubanks
##Decision structures, or branching structures.
##Sequence structures are the structures we earlier used, which always goes
##from the top of the code to the bottom, doing each line one at a time.
##Branching structures are questions that lead to yes or no questions, which
##answers are followed up by differing code lines being run.
##Decision structures are made of the keyword if, as well as a condition "then"
##A condition is composed of 1 or more boolean expressions.
##Boolean expressions structure: Operand 1, Relational Operator, Operand 2.
##Relational Operators are math statements: <, >, <=, >=, !=
##num_hours < 0
##Example of Boolean Expression
##num_hours > "12"
##This fails as a boolean expression, as it is considered a string instead.
##When multiple boolean expressions are used, combine via Logical Operators
##These are the words "and, or, not". Example on line 26
##Reserved words in python: True, False
##Condition must be followed by colon, as shown in line 26 and 20
num_hrs = int(input("Enter hours"))
if 0 <= num_hrs <= 20:
    print("Valid hours")
    ##The print statement indented here is in the "if block".
else:
    print("Invalid")
##First option for if statements is possible in python, but not recommended.
if num_hrs >= 0 and num_hrs<=20:
    print("OK")
else: ##Must be less than 0 or greater than 20. Write a comment on else and ifs.
    print("Not OK")
##This is another example of an if statement in a different example.
##Both have to be true to be valid! Statement must be used for CS majors.

print("..all ok.after if statement..")

##-1 error message and ok message
##0 ok message
##10 ok message
##lines 25,26,27 show output that is expected and shows programmer tested
##each result from the expression.
import random
##Imports a stored library that runs a random number.Period shows libraries
stu_points = random.randint(55,100)
print(f"stu_points = {stu_points}")
if stu_points>= 90:
    print (f"A! Fantastic!")
else: ##55-89.
    if stu_points >= 80:
        print(f"B! Good job!")
    else: ##55-79
        if stu_points >= 70:
            print(f"C! Just a little bit more!")
## Most efficient way to code these statements, but is hard to understand.
if stu_points >= 80 and stu_points <= 89:
    print(f"--A--")
##Another way to code the same statement.
