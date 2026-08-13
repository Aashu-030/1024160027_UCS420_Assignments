#Assignment 1.1: WAP to print your name three times 
print("Aarush Sareen")
print("Aarush Sareen")
print("Aarush Sareen")
print("Roll No: 1024160027")
#Assignment 2.1: WAP to add two numbers and print the result
a = 10
b = 20
c = 30
d = a + b + c
print(a, "+", b, "+", c , "=", d)
#Assignment 2.2: WAP to concatenate three strings and print the result
a = "Aarush"
b = "Sareen"
c = "1024160027"
d = a + " " + b + " " + c
print(a, " + ", b , "+", c, "-> ", d)
#Assignment 4.1: WAP to print table of 7, 9
print("Table of 7")
for i in range(1, 11):
  print(" 7 * ", i, "= ", i*7)
print("Table of 9")
for i in range(1, 11):
  print(" 9 * ", i, "= ", i*9)
#Assignment 4.2: WAP to print table of n, where n is user input
n = int(input("Enter any number: "))
print("Table of ", n)
for i in range(1, 11):
  print(n, "* ", i, "= ", i*n)
#Assignment 4.3: WAP to add all numbers from 1 to n, where n is user input
s = 0
n = int(input("Enter any number: "))
for i in range(1, n + 1):
  s = s + i
print("Sum is ->", s)
#Assignment 5.1: WAP to find max among three numbers, where numbers are user input
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("Max among three numbers is ->", max(a, b, c))
#Assignment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is user input
n = int(input("Enter any number: "))
s = 0
for i in range(1, n + 1):
  if i % 7 == 0 and i % 9 == 0:
    s = s + i
print("Sum of numbers divisible by both 7 and 9 is ->", s)
#Assignment 5.3: WAP to add all prime numbers from 1 to n and n is user input 
n = int(input("Enter any number: "))
s = 0
for i in range(2, n + 1):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    s = s + i
print("Sum of prime numbers from 1 to", n, "is ->", s)
#Assignment 6.1 : WAP using function that add all odd numbers from 1 to n, n is user input.
n = int(input("Enter any number: "))
def addOdd(n):
  s = 0
  for i in range(1, n+1):
    if i % 2 != 0:
      s = s+i
  return s
print("Sum of odd numbers from 1-", n, "is : ", addOdd(n))
#Assignment 6.2 : WAP using function that add all prime numbers from 1 to n, n given by the user.
n = int(input("Enter any number: "))
def addPrime(n):
  s = 0
  for i in range(2, n + 1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      s = s + i
  return s
print("Sum of prime numbers from 1-", n, "is : ", addPrime(n))
