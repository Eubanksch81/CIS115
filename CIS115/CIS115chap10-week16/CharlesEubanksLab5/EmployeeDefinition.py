##Charles Eubanks, Week 16, Lab 5

class Employee:
    __empName = "-na-"
    __idNumber = '0'
    __department = "-na-"
    __title = "-na-"
    
    def __init__(self, inp_empName, inp_idNumber, inp_dept, inp_title):
        self.__empName = inp_empName
        self.__idNumber = inp_idNumber
        self.__department = inp_dept
        self.__title = inp_title

    def setEmpName(self, inp_empName):
        self.__empName = inp_empName

    def setIdNumber(self, inp_idNumber):
        self.__idNumber = inp_idNumber

    def setDepartment(self, inp_dept):
        self.__department = inp_dept

    def setTitle(self, inp_title):
        self.__title = inp_title
    
    def getEmpName(self):
        return self.__empName
        
    def getIdNumber(self):
        return self.__idNumber
        
    def getDepartment(self):
        return self.__department

    def getTitle(self):
        return self.__title

    def __str__(self):
        ret_var = "\n Name       : " + self.__empName
        ret_var += "\n ID         : " + self.__idNumber
        ret_var += "\n Department : " + self.__department
        ret_var += "\n Title      : " + self.__title
        return ret_var

##Sample output
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\School\CIS115\CIS115chap10-week16\Week16Lab5\Chapter10_Lab_class_tester.py
##Employee 1:
## Name       : Susan Meyers
## ID         : 47899
## Department : Accounting
## Title      : Vice President
##
##Employee 2:
## Name       : Mark Jones
## ID         : 39119
## Department : IT
## Title      : Programmer
##
##Employee 3:
## Name       : Joy Rogers
## ID         : 81774
## Department : Manufacturing
## Title      : Engineer
##
##>>> 
        



