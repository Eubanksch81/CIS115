##Charles Eubanks, Assignment 3
##The purpose of this program is to calculate a salary for a person who works
##between 2 and 50 days, and for the salary to double each day.

days_wrk = int(input(f"Please input the amount of days worked. "))

while days_wrk < 2 or days_wrk > 50:
    print (f"Invalid input! Days must be between 2 and 50.")
    int(input(f"Please re-input days worked."))



