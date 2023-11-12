# Lab6
# Author:Jonathan Welch

#write a function that calculates the area of a rectangle given its width and height
    
def calculate_rectangle_area(width:float, height:float) -> float:
    """
    Args:
        width (float): width of rectangle
        height (float): height of rectangle
    Returns:
        float: area of rectangle
    """ 
    

    return width * height

import math 

def calculate_hypotenuse(side_a: float, side_b: float) -> float:
    """
    Args:
       side_a (float): Length of side a 
        side_b (float): length of side b
    Returns:
        float: Length of  the hypotenuse
    """ 
    return math.sqrt(side_a**2 + side_b**2)

def is_even(number: int) -> bool:
    """
    Args:
        number (int): number to check if even
    Returns:
        bool: True if even, False if odd
    """ 
    return number % 2 == 0

def find_maximum(number1: float, number2: float) -> float:
    """
    Args:
        number1 (float): first number to compare
        number2 (float): second number to compare
    Returns:
        float: maximum of number1 and number2
    """ 
    if number1 > number2:
        return number1
    else:
        return number2

def grade_calculator(score: float) -> str:
    """
    Args:
        score (float): score to calculate grade for
    Returns:
        str: grade for score
    """ 
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


## add in functions from test.py's test statements here to make the pytest work

def main():
    pass


if __name__ == "__main__":
    main()
