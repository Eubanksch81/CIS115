#test_Student_obj.py
from Week15student_definition import *
def main():
    student1 = Student("Maya", 2) ##invokes the __init__
##    student1.setStuName("maya")
##    student1.setStuID(200)
    print(f"student1 data: {student1}")

    print(f"student1 email: {student1.getEmailID()}")
    
main()
