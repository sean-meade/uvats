import workings
import time

"""
u = initial velocity
v = final velocity
a = acceleration
t = time
s = displacment

v = u + at
v** = u** + 2as
s = ut + 0.5(a)t**
s = vt - 0.5(a)t**
s = 0.5(u + v)t
"""

print("For the unknown values just press Enter.")
time.sleep(2)

u = float(input("initial velocity: "))
v = float(input("final velocity: "))
a = float(input("acceleration: "))
t = float(input("time: "))
s = float(input("distance: "))


def solveuvats(u, v, a, t, s):
    # When a, t and s are known.
    if (u == 0 and v == 0):
        nums = workings.uvZero(a, t, s)
        print(nums)

    # When a, t and v are known
    elif (u == 0 and a == 0):
        nums = workings.uaZero(v, t, s)
        print(nums)    
    
    # When a, v, and s are known
    elif (u == 0 and t == 0):
        nums = workings.utZero(a, v, s)
        print(nums)              
    
    elif (u == 0 and s == 0):
        nums = workings.usZero(v, a, t)
        print(nums)
        
    elif (v == 0 and a == 0):
        nums = workings.vaZero(t, s, u)
        print(nums) 

    elif (v == 0 and t == 0):
        nums = workings.vtZero(u, a, s)
        print(nums)
    
    elif (v == 0 and s == 0):
        nums = workings.vsZero(u, a, t)
        print(nums)

    elif (a == 0 and t == 0):
        nums = workings.atZero(u, v, s)
        print(nums)

    elif (a == 0 and s == 0):
        nums = workings.asZero(u, v, t)
        print(nums)

    elif (t == 0 and s == 0):
        nums = workings.tsZero(u, v, a)
        print(nums)

    else:
        print("not enough information to solve")

solveuvats(u, v, a, t, s)