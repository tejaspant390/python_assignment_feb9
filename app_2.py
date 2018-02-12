class Student:
    def __init__(self,initial,last):
        self.initial=initial
        self.last=last

    def emailGenerator(self):
        self.email=self.initial.lower()+'.'+self.last.lower()+"@gmail.com"


std= Student(input("Enter first name: "),input("Enter last name: "))
std.emailGenerator()
print("E-mail Id: " +std.email)
