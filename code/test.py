

#import necessary modules
import math

#define a function to display the numbers and symbols
def display(num):
    print(num)

#define a function to get user input
def get_input():
    num = input("Enter a number or symbol: ")
    return num

#define a function to store and recall numbers and calculations
def memory(num):
    memory_list = []
    memory_list.append(num)
    return memory_list

#define a function to perform basic calculations
def calculations(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

#define a function to perform trigonometric calculations
def trig_calculations(num, operator):
    if operator == "sin":
        return math.sin(num)
    elif operator == "cos":
        return math.cos(num)
    elif operator == "tan":
        return math.tan(num)

#define a function to calculate the square root
def square_root(num):
    return math.sqrt(num)

#main program
while True:
    num = get_input()
    display(num)
    memory_list = memory(num)
    if num == "+" or num == "-" or num == "*" or num == "/":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = calculations(num1, num2, num)
        print("Result: ", result)
    elif num == "sin" or num == "cos" or num == "tan":
        num = float(input("Enter the number: "))
        result = trig_calculations(num, num)
        print("Result: ", result)
    elif num == "sqrt":
        num = float(input("Enter the number: "))
        result = square_root(num)
        print("Result: ", result)
    else:
        print("Invalid input")