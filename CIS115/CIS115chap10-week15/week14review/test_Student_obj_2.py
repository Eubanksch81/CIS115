#test_Student_obj.py
from Student_definition import *
def main():
    student1 = Student()  
    student2 = Student() 

    print(f"student1 data: {student1}")

    student1.setStuName("maya")
    print(f"student1 data: {student1}")
    
main()
