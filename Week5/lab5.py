# Lab5
# Author:Jonathan Welch 


# Part 1: Create a function called 'greet' that takes a 'name' as an argument
# and prints a greeting message with the name. Use a default value of "Guest" for the name.
name =("Guest")
def greet(name):
    print("Hello", name)
# Part 2: Create a function called 'calculate_area' that calculates the area of a rectangle.
# It should take two parameters: 'length' and 'width' with default values of 0.
# The function should return the area (length * width).
calculate_area = 0
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 5))


# Part 3: Create a main method that demonstrates the usage of the greet function and the calculate_area function.
# You can either take in the inputs from the user or hardcode them in the main method.

def main():
    name = input("Enter your name:")
    greet(name)
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    print("The area is", calculate_area(length, width))

if __name__ == "__main__":    
    main()

