##Charles Eubanks, CIS115, Mrs. Tolappa, Assignment 4
##Goal is to modify the incomplete file to include a failing letter symbol to
##each person whose score is less than 60, as well as to count each person who
##failed and present a percentage of students who passed.

def main():
    file_students = open("student_points.txt", "r")
    stu_name = file_students.readline()  #read the first record,
                                        #which is the first student's name
    num_stu = 0
    num_fail = 0
    num_pass = 0
    print(f"Student              Points    Grade")
    print("-------------------------------------\n")
    while stu_name != "":
        stu_name = stu_name.rstrip("\n")        #strip \n from name
        stu_points = file_students.readline()#read numeric points
        stu_points = int(stu_points)            #cast points into an int
        if stu_points < 60:  ##Reads each point value and checks
                                ##if each one is >60
            fail_score = "--F--"
            num_fail += 1
        else:
            fail_score = ""
        print(f"{stu_name:15}        {stu_points}     {fail_score}")
        num_stu += 1
        num_pass = num_stu - num_fail
        
        stu_name = file_students.readline()
    perc_pass = (num_pass / num_stu) * 100
    file_students.close()
    print()
    print(f"Number of students processed = {num_stu}")
    print(f"Number of students failed = {num_fail}")
    print(f"% of students passed = {perc_pass:.1f}%")

main()

##Sample output:
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap7-week12\Week12Assign4\chapter06_assignment.py
##Student              Points    Grade
##-------------------------------------
##
##Johnson Smith          93     
##Maryanne James         80     
##Stanton Chase          45     --F--
##Mildred Morris         90     
##George Deitz           58     --F--
##Maisie Kling           79     
##
##Number of students processed = 6
##Number of students failed = 2
##% of students passed = 66.7%
##>>> 
