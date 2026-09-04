class Employee():
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print("role= ",self.role,", department= ", self.dept, ", salary= ",self.sal)

e1=Employee("Accountant","Finance","15 LPA")
e1.showDetails()

class Engineer(Employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("developer","IT","25 LPA")

    def show(self):
        print("The name is: ",self.name,",the age: ",self.age)

en1=Engineer("Anshu","22")
en1.show()
en1.showDetails()
        