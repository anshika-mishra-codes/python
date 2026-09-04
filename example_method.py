class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        total=0
        for x in self.marks:
            total=total+x
        avg=total/3
        print("Hi",self.name,"your average is: ", avg)

s1=Student("Anshu",[99,98,97])
s1.average()