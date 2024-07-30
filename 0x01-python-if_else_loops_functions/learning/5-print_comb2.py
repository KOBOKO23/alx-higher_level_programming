'''
prints numbers from 0 to 99

'''

for num in range(100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=', ')
