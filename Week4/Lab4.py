# Lab3
# Author: Jonathan Welch 

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
input_number = int(input("Enter a number: "))
if input_number > 0:
        print("Positive")
elif input_number < 0:
        print("Negative")
else:
    print("Zero")

# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
input_number = int(input("Enter a number: "))
remainder = input_number % 2
if remainder == 0:
    print("Even")
else:
    print("Odd:", remainder)

# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
input_number = int(input("Enter a number: "))
counter = 1
while counter <= input_number:
    print(counter)
    counter += 1
print("Done")
# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
sum = 0
for i in range(5):
    number = int(input("Enter a number: "))
    sum += number
    sum+=input_number
average = sum / 5 
print(average)   
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
input_number = int(input("Enter a number: "))
counter = input_number
while counter >= 1:
    import time
    time.sleep(1)  
    print(counter)
    counter -= 1
print("blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.

input_number = int(input("Enter a number: "))
for i in range(1, input_number + 1):
    if i % 7 == 0:
        print("Lucky")
        continue
    if i > 100:
        break
    print(i)