##Charles Eubanks, Week 16, Assign 5

class Car:
    __make_model = ""
    __year = ""
    __speed = 0
        
    #my_car = CarDefinition.Car("2008", "Honda Accord")
    def __init__(self, param_year, param_make_model):
        self.__make_model = param_make_model
        self.__year = param_year
        self.__speed = 0

    ############# make_model################
    def setMake_model(self, param_make_model):
        self.__make_model = param_make_model

    def getMake_model(self):
        return self.__make_model

    ############# Make################
    def setYear(self, param_year):
        self.__year = make

    def getYear(self):
        return self.__year
    
    ############# speed################
    def setSpeed(self, inp_speed):
        if inp_speed < 0 or inp_speed > 130:
            print(f"Speed cannot be {inp_speed} mph.",
                  "Speed be must be 0-130 mph")
        else:
            self.__speed = inp_speed

    def getSpeed(self):
        return self.__speed

    
    ############## accelerate function ############
    
    def accelerate(self):
        
  
    
    ############## brake function ################

    ############# str ############
    def __str__(self):
        ret_val = f"Year : {self.__year}"
        ret_val += f", Make and Model : {self.__make_model}"
        ret_val += f", Speed : {self.__speed}"
        return ret_val
