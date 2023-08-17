import math


def minus_b(a, b, c):
    """
    Where a, b, and c are all values from a quadratic equation
    ax^2 + bx + c = 0
    and a != 0
    """
    
    bottom = 2*(a)
    topPositive = math.sqrt((b**2 - (4 * a * c))) - b
    topNegative = -(math.sqrt((b**2 - (4 * a * c)))) - b

    positiveRoot = topPositive/float(bottom)
    negativeRoot = topNegative/float(bottom)

    return positiveRoot, negativeRoot