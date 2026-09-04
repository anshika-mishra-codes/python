class Circle():
    
    def __init__(self,r):
        self.radius=r
        self.pie=3.14

    def area(self):
        self.ar= self.pie * ((self.radius)**2)
        print("area is: ", self.ar)

    def peri(self):
        self.perimeter= 2 * self.pie * self.radius
        print("the perimeter is :", self.perimeter)


c1=Circle(21)
c1.area()
c1.peri()
