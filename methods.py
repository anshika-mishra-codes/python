class Student:
    college="RRSIMT"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def welcome(self):
        print("Welcome",self.name,"!")

    def get_marks(self):
        return self.marks

s1= Student("Anshu",98)
print(s1.get_marks())
s1.welcome()


    