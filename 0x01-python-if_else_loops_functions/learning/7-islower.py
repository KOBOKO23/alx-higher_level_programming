'''
a function that checks for lowercase character.

'''

def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    return False
