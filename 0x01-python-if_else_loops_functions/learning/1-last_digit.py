import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
"""
prints the last digit of a random number
each time the prog is executed. """

if number < 0:
    number = number * -1

last_digit = number % 10

if last_digit == 0:
    print("The last digit of {} is {} and is 0".format(number, last_digit))

elif last_digit > 5:
    print("The last digit of {} is {} and is greater than 5".format(number, last_digit))

else:
    print("The last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
    
