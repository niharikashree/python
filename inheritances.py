#INHERITANCES
#SINGLE LEVEL INHERITANCE
class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class Box2(Box):
    def __init__(self,name,rollno,marks):
        self.marks=marks
        Box.__init__(self,name,rollno)

obj=Box2("niharika",30,98)
print(obj.name)
print(obj.rollno)
print(obj.marks)



#MULTIPLE LEVEL INHERITANCE
class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class student:
    def __init__(self,fees):
        self.fees=fees
class Box2(Box,student):
    def __init__(self,name,rollno,marks,fees):
        self.marks=marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollno)

obj1=Box2("Meghana",45,85,45000)
print(obj1.name)
print(obj1.rollno)
print(obj1.marks)
print(obj1.fees)



#  MULTI LEVEL INHERITANCE
class Box:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class student:
    def __init__(self,fees):
        self.fees=fees
class Box2(Box,student):
    def __init__(self,name,rollno,marks,fees):
        self.marks=marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollno)

class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"Anirudh",65,89,25000)

obj3=Box3(3)
print(obj3.name)
print(obj3.rollno)
print(obj3.marks)
print(obj3.fees)
print(obj3.sem)
