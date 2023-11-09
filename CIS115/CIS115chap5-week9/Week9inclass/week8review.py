##Charles Eubanks, Week 8, Functions
##Functions are used to prevent copy and paste, and to allow the program to
##be in smaller chunks to view/modify.
##There are two main ideas to work with in functions.
##The function must be defined, and used. (Invoked, Called, invocated, executed)
##To define the function, it must have a function header and body.
##In python, the header must start with the word "def".
##Then, the function must be named. Same rules as naming variables.
##Up next is the parameter list. Enclose the parameters in (), if no parameters
##then just do a blank (). Then place a colon
##After that is the function body. The statements that follow the header.
##Its placed after the indent, and atleast one statement is required in the body
##In C++ and Java, everything is placed within functions.
##the word "main" marks the main function, where the program starts.

def display():
    print(f"display")

def main():
    print(f"Hello world!")
    display()
##    main() again causes an infinite recursion.
    main2()
    age = int(input(f"What is your age? "))
    main3(age)

##main() ##This calls the function. Executes line 20, 16, 17, 18, 21
##Functions cannot have the same name as variables.
print(f"--End--")

##Variables and functions
stu_name = input(f"Enter Name: ") ##Example of global variable, BAD
def main2():
    print(f"Hello {stu_name}")
    disp_bye()

def disp_bye():
    print(f"Goodbye {stu_name}")
    age = int(input(f"What is your age? "))
    main3(age) ##Invokes function with 1 arguement which is a local variable.

##Variables also require scope and duaration.
##Scope is where a variable can be used
##Local scope is perferred, where the variable is defined WITHIN a function,
##and can only be used in that function. Global variables are variables that
##are defined outside the function, and can be used anywhere. They're prohibited.
##Duration is how long the variable is active
##Local variable example

##Function takes in a parameter.
##Parameter is considered a local variable
def main3(_age):
    stud_lastname = input(f"What is your last name? ")
    print (f"Hello Mr. {stud_lastname}")
    print(_age)

disp_bye()
#main3(_age)
