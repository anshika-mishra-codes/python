class Student():
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

        # def calcPercentage(self):
        #     self.percentage= str(self.phy + self.chem + self.maths) +"%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/ 3 )+"%"

st1=Student(98,97,99)
print(st1.percentage)

st1.phy= 86
print(st1.percentage)
