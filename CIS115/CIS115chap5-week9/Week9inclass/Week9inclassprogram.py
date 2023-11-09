##Charles Eubanks, Probably more functions

##Pass by value makes a copy of a variable when sending it between functions.
##Pass by reference uses the genuine variable from a seperate function.
##Pass by value is slower, but safer as it doesn't change the original variable.
##Pass by reference is faster, but it changes the original variable.

##def main():
##    stu_name = input("Enter name: ")
##    disp_bye(stu_name)
##    week_num = "Week # 16"
##    disp_bye(week_num)
##
##def disp_bye(param):
##    print(param)
import random
def main():
    randomNumber1 = random.randint(0,100)
    randomNumber2 = random.randint(0,100)
    randomNumber3 = random.randint(0,100)
    print_num("randomNumber1", randomNumber1)
    print_num("randomNumber2", randomNumber2)
    print_num("randomNumber3", randomNumber3)
    total_score = 100
    total_score = get_total(randomNumber1, randomNumber2)
    main2()

def get_total(p_random1, p_random2):
    total_param = p_random1 + p_random2
    print(total_param)

def main2():
    randomNumber4 = random.randint(0,100)
    randomNumber5 = random.randint(0,100)
    randomNumber6 = random.randint(0,100)
    print_num("randomNumber4", randomNumber4)
    print_num("randomNumber5", randomNumber5)
    print_num("randomNumber6", randomNumber6)

def print_num(param_str, param_int):
    print(f"{param_str} contains {param_int}")
    
main()
