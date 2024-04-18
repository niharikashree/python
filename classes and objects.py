CLASSES AND OBJECTS

class Box:
    def __init__(self, currname,currrolno,currdbms,curros,currjava,currds,currc):
        self.name=currname
        self.rolno=currrolno
        self.dbmsmarks=currdbms
        self.osmarks=curros
        self.javamarks=currjava
        self.dsmarks=currds
        self.cmarks=currc

#OBJECT CREATION
student1 = Box("sita",898,67,68,98,96,99)
student2 = Box("SreeRama",988,78,79,89,98,95)
print(student1.name)
print(student1.cmarks)
print(student1.rolno)

print(student2.name)
print(student2.cmarks)
print(student2.rolno)





class card:
    def __init__(self,image,price,rating,description,deliverywithin,comments,brandname):
        self.imageurl=image
        self.price=price
        self.rating=rating
        self.decp=description
        self.delivery=deliverywithin
        self.comments=comments
        self.brand=brandname
    
    def printalldetails(self):
        print(self.imageurl)
        print(self.price)
        print(self.rating)
        print(self.decp)
        print(self.delivery)
        print(self.comments)
        print(self.brand)


card1=card("c:\ihnj\fhgjk\flipkart",89999,4.5,"product based description","15 days","its a satisfiable product","Versace")
shoe=card("jf\rufhoeu\amazon",5600,4.9,"soft and foamy footware"," 6 weeks","very comfortable wear ","NIKE")

card1.printalldetails()
shoe.printalldetails()




class Box:
    def __init__(self,name,rollno,dbmsmarks,pythonmarks,cmarks,osmarks,cnmarks):
        self.name=name
        self.rolno=rollno
        self.dbms=dbmsmarks
        self.python=pythonmarks
        self.c=cmarks
        self.os=osmarks
        self.cn=cnmarks
    def printall(self):
        print(self.name)
        print(self.rolno)
        print(self.dbms)
        print(self.python)
        print(self.c)
        print(self.os)
        print(self.cn)


student1=Box("Harika","5A1",78,67,77,89,46)
student2=Box("Swapna","5A2",38,65,97,59,41)
student3=Box("Sushma","5A3",88,95,47,89,31)
student1.printall()
student2.printall()
student3.printall()
