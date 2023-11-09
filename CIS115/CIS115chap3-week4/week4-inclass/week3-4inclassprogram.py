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

stu_name = input("Enter Name") #"Charles"
##just inputting would allow any characters.
stu_hours = int( input("Enter hours") ) #15
##using int only alllows numerical integers to be entered.
##Make sure to use 2 paranthesis while using int!

print(f"Hello {stu_name}. You are taking {stu_hours} hours.")

stu_hours_new = stu_hours * 2
print(f"Hours now = {stu_hours_new}")

##Week 4
semester_name = "Fall 2021"
stu_gpa_str = input("Enter GPA")
stu_gpa = float(stu_gpa_str)
##This is an alternate version of the int statement used earlier.

