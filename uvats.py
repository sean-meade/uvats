"""
u = initial velocity
v = final velocity
a = acceleration
t = time
s = displacment

v = ut + 0.5(a)t**
v** = u** + 2as
s = ut + 0.5(a)t**
s = vt - 0.5(a)t**
s = 0.5(u + v)t
"""

import math

"""u = int(input("initial velocity: "))
v = int(input("final velocity: "))
a = int(input("acceleration: "))
t = int(input("time: "))
s = int(input("distance: "))"""

def solveuvats(u, v, a, t, s):
    # When a, t and s are known.
    if (u == 0 and v == 0):
        # solve for u
        u = (s - (0.5 * a * (t ** 2)))/t
        # solve for v
        v = math.sqrt( u ** 2 + 2 * a * s)

    elif (u == 0 and a == 0):
        # solve for u
        u = (2 * s - v * t) / t
        # solve for a
        a = ((v**2 - u**2) / (2 * s))
    
    """elif (u = 0 & t = 0):
    
    elif (u = 0 & s = 0):
        
    elif (v = 0 & a = 0):

    elif (v = 0 & t = 0):
    
    elif (v = 0 & s = 0):

    elif (a = 0 & t = 0):

    elif (a = 0 & s = 0):

    elif (t = 0 & s = 0):

    else:
        print("not enough information to solve")"""

    print(u, v, a, t, s)

solveuvats(0, 10, 0, 10, 20)