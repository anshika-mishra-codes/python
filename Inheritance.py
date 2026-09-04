# inheritance, there are 3 types(1. single inheritance,where there is only one parent class and one child class)-

class Car():   # parent class
    @staticmethod
    def start():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("car has stopped.... ")

class Hyundai_Cars(Car): # child class

    def __init__(self,brand):
        self.brand=brand

c1=Hyundai_Cars("Creta")
c2=Hyundai_Cars("Aura")

#using the child class's attributes

print(c1.brand)
print(c2.brand) 

# now using the parents class attribute through the child class

c1.start()
c1.stop()

# now we are doing 2. multi-level inheritance, where there is multiple level of inheritance, the child class inherits from the parent class,
# car and hyundai cars respectively, and then another class inherits from the child class,
# and it becomes grandchild {not a technical term} of the cars {the original parent class}

print("\nnow this output is for Creta class---")

class Creta(Hyundai_Cars): #this is a child class of the hyundai cars and grandchild of the cars class
    color="White"
    def __init__(self,fuel_type):
        
        self.fuel_type=fuel_type
        
cr1= Creta("Diesel")
print(cr1.color)
cr1.start()
print(cr1.fuel_type)
cr1.stop()

# now there comes 3. Multiple inheritance where a child class can inherit from multiple parent classes
print("\nnow output is for venue class")

class Engine():
        engine_type="petrol_engine"

class Venue(Creta,Engine): #parents are car and creta classes
    def __init__(self,seats):
        self.seats=seats
            
v1= Venue(5)
v1.start() #from parent 1 ,car
# print(v1.color) # from parent 2, creta
print(v1.seats)
print(v1.engine_type)
v1.stop()