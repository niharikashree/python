#EXCEPTIONS 
print("starting line")
ar=[12,34,63,98]

try:
    a=10/5
except:
    print("some exceptions raised")
else:
    print("no exception raised,everything worked perfectly")
try:
     print(ar[5])
     print(y)
except:
    print("ArrayIndexOutOfbound exception")
else:
    print("no exception raised,everything worked perfectly")
finally:
    print("this is a final block")




#ANOTHER EXAMPLE
print("starting line")
ar=[12,34,63,98]

try:
    a=10/0
except ZeroDivisionError:
    print("exceptions raised due to zero division error")
except IndexError:
    print("exceptions raised due to index out of bound error")
except NameError:
    print("exceptions raised due to unidentified variable")
else:
    print("no exception raised,everything worked perfectly")
finally:
    print("this is a final block")
print("ebverything will execute now")

