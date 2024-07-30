import random
number = random.randint(-10, 10)
# YOUR CODE HERE

""" prints a random number each time the

the code is executed """

if number > 0:
    print("The number is {} and is positive".format(number))

elif number == 0:
    print("The number is {} and is zero".format(number))

else:
    print("The number is {} and is negative".format(number))
