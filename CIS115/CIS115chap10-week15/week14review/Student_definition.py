#Student_definition.py
class Student:
    __stuName = "-not set-"  
    __stuId = 0     

    def __init__(self):
        print("from init")

    def setStuName(self, param_name):
        if param_name == "":
            print("Name cannot be blank")
        else:
            self.__stuName = param_name
        
       
    def __str__(self):
        ret_var = "Name = " + self.__stuName
        ret_var += ", ID = " + str(self.__stuId) 
        
        return ret_var
       
