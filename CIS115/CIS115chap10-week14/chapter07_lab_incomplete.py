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
