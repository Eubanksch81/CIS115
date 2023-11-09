##Charles Eubanks, Week 14, Lab 4

import random
def main():
    size = 11
    lst_stu_names = ["Vernon", "Domenic", "Michael", "Celena",
                    "Odis", "Rufus", "Rose", "Cheryll",
                     "Mignon", "Monte", "Ralph"]

    lst_stu_grades = [""] * size

    for i in range(size):
         lst_stu_grades[i] = random.choice(["A", "B", "C", "D", "F"])

    num_A_stu = 0
    num_B_stu = 0
    totalRecord = 0
    
    print(" # Student\tGrade\n--------------------------")
##Do not change lines 1 - 17

    for i in range(size):
        totalRecord += 1
        grade = lst_stu_grades[i]
        st_name = lst_stu_names[i]
##        message = " "
        if grade == "A":
            message = "**"
            num_A_stu += 1
        else:
            if grade == "B":
                message = "*"
                num_B_stu += 1
            else:
                message = "  "

        print(f"{totalRecord:>2d}. {st_name:<11}\t{grade}\t{message}")

    print()
    print(f"Total Students   : {size:>2}")
    print(f"A Students     : {num_A_stu:>2} ({num_A_stu/totalRecord:>.1%})")
    print(f"B Students     : {num_B_stu:>2} ({num_B_stu*100/totalRecord:>.1f}%)")
    print(f"A and B Students: {num_A_stu+num_B_stu:>2} ({(num_A_stu+num_B_stu)/totalRecord:>.1%})")

main()

##Sample output from 3 tests:
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\School\CIS115\CISchap10-week14\Charleschapter07_lab_complete.py
## # Student	Grade
##--------------------------
## 1. Vernon     	A	**
## 2. Domenic    	C	  
## 3. Michael    	D	  
## 4. Celena     	B	*
## 5. Odis       	F	  
## 6. Rufus      	F	  
## 7. Rose       	A	**
## 8. Cheryll    	C	  
## 9. Mignon     	C	  
##10. Monte      	D	  
##11. Ralph      	F	  
##
##Total Students   : 11
##A Students     :  2 (18.2%)
##B Students     :  1 (9.1%)
##A and B Students:  3 (27.3%)
##>>> 
##= RESTART: C:\Users\Owner\Downloads\School\CIS115\CISchap10-week14\Charleschapter07_lab_complete.py
## # Student	Grade
##--------------------------
## 1. Vernon     	C	  
## 2. Domenic    	A	**
## 3. Michael    	D	  
## 4. Celena     	C	  
## 5. Odis       	C	  
## 6. Rufus      	B	*
## 7. Rose       	F	  
## 8. Cheryll    	C	  
## 9. Mignon     	A	**
##10. Monte      	A	**
##11. Ralph      	A	**
##
##Total Students   : 11
##A Students     :  4 (36.4%)
##B Students     :  1 (9.1%)
##A and B Students:  5 (45.5%)
##>>> 
##= RESTART: C:\Users\Owner\Downloads\School\CIS115\CISchap10-week14\Charleschapter07_lab_complete.py
## # Student	Grade
##--------------------------
## 1. Vernon     	A	**
## 2. Domenic    	D	  
## 3. Michael    	D	  
## 4. Celena     	A	**
## 5. Odis       	C	  
## 6. Rufus      	C	  
## 7. Rose       	C	  
## 8. Cheryll    	F	  
## 9. Mignon     	A	**
##10. Monte      	F	  
##11. Ralph      	A	**
##
##Total Students   : 11
##A Students     :  4 (36.4%)
##B Students     :  0 (0.0%)
##A and B Students:  4 (36.4%)
##>>> 
