class car:
    def __init__(self):
        self.acc=False
        self.brake=False
        self.clutch=False

    
    def start(self):
        self.acc=True
        self.brake=True
        self.clutch=True   
        print("car started...")   
     

s1=car()
s1.start()