class Student:
    college_name="ABC college"

    def __init__(self,name,marks):
        self.name= name
        self.marks=marks
        print("updating database...")
        
s1=Student("Anshu",99)
print(s1.name, s1.marks)

s2=Student("Anyone",56)
print(s2.name,s2.marks)

print(s2.college_name)
print(Student.college_name)