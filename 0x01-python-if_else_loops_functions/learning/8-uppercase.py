'''
prints a string in upper case

'''

def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            #convert the string to upper case

            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
