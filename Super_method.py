class Car():
    def __init__(self,type):
            self.type = type

    @staticmethod
    def start():
        print("starting the car......")

    @staticmethod
    def stop():
        print("the car stopped.....")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()


c1=ToyotaCar("prius","electric")
print(c1.name)
print(c1.type)