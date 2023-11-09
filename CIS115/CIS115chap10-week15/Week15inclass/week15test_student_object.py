#test_Student_obj.py
from Week15student_definition import *
def main():
    student1 = Student() ##invokes the __init__  
    ##0 parameters, so __init__ has one arguement.

    print(f"student1 data: {student1}") ##__str__

    student1.setStuName("maya") ##get fn for name
    print(f"student1 data: {student1}") ##__str__

    print(student1.getStuName) ##get for name

    student1.setStuID(-1) ##set for ID
    
main()
