'''
a program that prints all possible different combinations of two digits

'''

for i in range(10):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=', ')
