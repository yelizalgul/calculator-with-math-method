#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
       return "Cannot divide by zero!"
    else:
        return x / y

def modulus(x, y):
    if y == 0:
       return  "Cannot calculate mod number!"
    else:    
      return x % y

def square_root(x):
  if x < 0:
        return "Cannot calculate square root of a negative number!"
  else:
        return math.sqrt(x)
    

def exponentiation(x, y):
    return x ** y

def factorial(x):
    return math.factorial(x)

while True:
    print("Operation Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square Root")
    print("7. Exponentiation")
    print("8. Factorial Calculation")
    print("9. Exit")

    choice = input("Please select the operation you want to perform (1-9):")

    if choice == '9':
        print("Exiting the program...")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
    elif choice in ('6', '8'):
        num1 = int(input("Enter the number:"))

    if choice == '1':
        print("Result:", addition(num1, num2))

    elif choice == '2':
          print("Result:", subtraction(num1, num2))

    elif choice == '3':
          print("Result:", multiplication(num1, num2))

    elif choice == '4':
          print("Result:", division(num1, num2))

    elif choice == '5':
          print("Result:", modulus(num1, num2))

    elif choice == '6':
          print("Result:", square_root(num1))

    elif choice == '7':
          num2 = int(input("Enter the exponent:"))
          print("Result:", exponentiation(num1, num2))

    elif choice == '8':
          print("Result:", factorial(int(num1)))
    else:
        print("Invalid choice!")


# In[ ]:




