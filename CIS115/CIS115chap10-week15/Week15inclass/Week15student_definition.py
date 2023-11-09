#Student_definition.py
class Student:
    __stuName = "-not set-"  
    __stuID = 0     

    def __init__(self, param_name, param_id):
        self.__stuName = "-not set-"
        self.__stuID = 100  ##Gives default values first.
        
        self.setStuName(param_name)
        ##Sends variables to other functions to validate the data.
        self.setStuID(param_id)

    def getEmailID(self):
        ret_val = f"{self.__stuName} - {self.__stuID}@wcc.edu"
        return ret_val

    def setStuName(self, param_name):
        if param_name == "":
            print("Name cannot be blank")
        else:
            self.__stuName = param_name

    def getStuName(self):
        return self.__stuName

##must provide proof. -1, 100, 250, 999, 54563
    def setStuID(self, param_id):
        if param_id > 999 or param_id <= 100: ##100 to 999
            self.__stuID = param_id
        else:
            print(f"ID must be between 100 to 999.")

    def getStuID(self):
        return self.__stuID
       
    def __str__(self):
        ret_var = "Name = " + self.__stuName
        ret_var += ", ID = " + str(self.__stuID) 
##ret_var = f"name = {self.__stuName}, ID = {self.__stuID}" ##same thing as 2 above
        return ret_var
       
