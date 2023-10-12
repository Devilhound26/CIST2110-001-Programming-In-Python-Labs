# Lab5
# Author:Jonathan Welch 


# Part 1: Create a function called 'greet' that takes a 'name' as an argument
# and prints a greeting message with the name. Use a default value of "Guest" for the name.
name = "Guest"
def greet(name):  
    print("Welcome to this code", name)
# Part 2: Create a function called 'calculate_area' that calculates the area of a rectangle.
# It should take two parameters: 'length' and 'width' with default values of 0.
# The function should return the area (length * width).
calculate_area = 0
def calculate_area(length, width):
    return length * width
# Part 3: Create a main method that demonstrates the usage of the greet function and the calculate_area function.
# You can either take in the inputes from the user or hardcode them in the main method.
name ="Jonathan"
def main():
    greet(name)
    print(calculate_area(3, 4))
def calculate_area(length, width):
    return length * width
