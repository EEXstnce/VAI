

#import necessary modules
import math

#define functions
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def power(x, y):
   return x ** y

def root(x, y):
   return x ** (1/y)

#take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Root")

choice = input("Enter choice(1/2/3/4/5/6):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   print(num1,"**",num2,"=", power(num1,num2))

elif choice == '6':
   print(num1,"**(1/",num2,")=", root(num1,num2))

else:
   print("Invalid input")