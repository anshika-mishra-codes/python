# example 1(accessing the private attribute directly {gives error})---

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1=Account("12345","abcdef")

print(acc1.acc_no)
# print(acc1.__acc_pass) {commented out cause this instruction causes the error}
acc1.reset_pass()


# example 2 (where the private attribute is being accessed through another method {no error})--

class Person:
    __name="Anonymous"

    def __hello(self):
        print("Hello Person !")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())