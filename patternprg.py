#PATTERN ONE
n = int(input())
for i in range(1, n + 1):
   for star in range(i):
       print("*", end = "")
   print()

#PATTERN TWO
n = int(input())
for i in range(n):
   for j in range(n):
       print("*", end = "")
   print()

#PATTERN THREE
n = int(input())
spaces = 0
for i in range(n):
   for space in range(spaces):
       print(" ", end = "")
   for star in range(n):
       print("*", end = "")
   spaces += 1
   print()

#PATTERN FOUR
n = int(input())
for i in range(n, 0, -1):
   for star in range(i):
       print("*", end = "")
   print()

#PATTERN FIVE
n = int(input())
spaces = n - 1
stars = 1
for i in range(1, n + 1):
   for space in range(spaces):
       print(" ", end = "")  
   spaces -= 1
   for star in range(stars):
       print("*", end = "")
   stars += 1
   print()

#PATTERN SIX
n = int(input())
spaces = n - 1
for i in range(1, n + 1):
      
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
  
   for j in range(1, i + 1):
       print(j, end = "")
   print()

#PATTERN SEVEN
n = int(input())
for i in range(1, n + 1):
   for j in range(1, i + 1):
       print(j, end = "")
   print()
