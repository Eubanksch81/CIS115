##Charles Eubanks, Week 3, example 1, variables

##number_of_students snake case
##NumberOfStudents camel case
##numberofstudents These are all different styles to write variables.

##typically written like this:
##num_stu
##nbr_stu
##numb_stu

num_stu = 30

##var asn. op.       expression
num_stu = 24 + 30

print("num_stu",num_stu)

avg_score = (13 + 15) / 3

print(avg_score)

print(f"Number of Students = {num_stu}",end = ", ")
#the end argument makes it so that the print functions are coded seperately,
#but appear on the same line. 
print (f"Average Score = {avg_score:.1f}")
##The .1f at the end makes the amount only move to the first decimal.

stu_name = input("Enter Name") #"Charles"
stu_hours = int( input("Enter hours") ) #15

print(f"Hello {stu_name}. You are taking {stu_hours} hours.")

stu_hours_new = stu_hours * 2
print(f"Hours now = {stu_hours_new}")

price = int(68.549)
print(price)


