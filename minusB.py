import math

"""print("Find the roots of your quadratic!")
print("This is not set up for complex roots as of yet.")
print("ax^2 + bx + c = 0")
print("Don't forget the + or - sign when entering values")

a = int(input("Please enter the a value: "))
b = int(input("Please enter the b value: "))
c = int(input("Please enter the c value: "))"""

def minusB(a, b, c):
    bottom = 2*(a)
    topPositive = math.sqrt((b**2 - (4 * a * c))) - b
    topNegative = -(math.sqrt((b**2 - (4 * a * c)))) - b

    positiveRoot = topPositive/float(bottom)
    negativeRoot = topNegative/float(bottom)

    """print("Your first root is: ", positiveRoot)
    print("Your second root is: ", negativeRoot)"""

    return(positiveRoot, negativeRoot)

"""minusB(a, b, c)
"""
