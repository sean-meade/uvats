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

u = (input("initial velocity: "))
v = (input("final velocity: "))
a = (input("acceleration: "))
t = (input("time: "))
s = (input("distance: "))

def solveuvats(u, v, a, t, s):
    listOfInputs = [u, v, a, t, s]
    convertedInputs = []

    for i in listOfInputs:
        if i == '':
            convertedInputs.append(i)
        else:
            i = float(i)
            convertedInputs.append(i)

    u = convertedInputs[0]
    v = convertedInputs[1]
    a = convertedInputs[2]
    t = convertedInputs[3]
    s = convertedInputs[4]

    # When a, t and s are known.
    if (u == '' and v == ''):
        nums = workings.uvZero(a, t, s)
        print(nums)

    # When a, t and v are known
    elif (u == '' and a == ''):
        nums = workings.uaZero(v, t, s)
        print(nums)    
    
    # When a, v, and s are known
    elif (u == '' and t == ''):
        nums = workings.utZero(a, v, s)
        print(nums)              
    
    elif (u == '' and s == ''):
        nums = workings.usZero(v, a, t)
        print(nums)
        
    elif (v == '' and a == ''):
        nums = workings.vaZero(t, s, u)
        print(nums) 

    elif (v == '' and t == ''):
        nums = workings.vtZero(u, a, s)
        print(nums)
    
    elif (v == '' and s == ''):
        nums = workings.vsZero(u, a, t)
        print(nums)

    elif (a == '' and t == ''):
        nums = workings.atZero(u, v, s)
        print(nums)

    elif (a == '' and s == ''):
        nums = workings.asZero(u, v, t)
        print(nums)

    elif (t == '' and s == ''):
        nums = workings.tsZero(u, v, a)
        print(nums)

    else:
        print("not enough information to solve")

solveuvats(u, v, a, t, s)