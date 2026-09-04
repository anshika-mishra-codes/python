class Person:
    name="anonymous"

    def changeName (self, name):
        Person.name = name                 #first way to change a class attribute
        self.__class__.name = "Anshu"      #second way

    # and now 3rd way to change a class attribute is class method
    @classmethod
    def new_Name (cls, name):
        cls.name = name 


        
p1=Person()
p1.changeName("Anshu Mishra")

print("the output of first way: ",Person.name)

print("the output of second way: ",p1.name)  

p1.new_Name("Somebody")   #calling the classmethod with a new name

print(p1.name)


