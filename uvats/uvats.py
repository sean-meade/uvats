from .workings import *
import time


def solve_uvats_with_user_input():
    """
    Takes user input and solves for the missing values
    """

    print("For the unknown values just press Enter.")
    time.sleep(2)

    u = (input("initial velocity: "))
    v = (input("final velocity: "))
    a = (input("acceleration: "))
    t = (input("time: "))
    s = (input("distance: "))

    return solve_uvats(u, v, a, t, s)

def solve_uvats(u, v, a, t, s):
    """
    Takes 3 values from the following
        u = initial velocity
        v = final velocity
        a = acceleration
        t = time
        s = displacment

    and solves for the other two using the formula:

        v = u + at
        v** = u** + 2as
        s = ut + 0.5(a)t**
        s = vt - 0.5(a)t**
        s = 0.5(u + v)t

    """

    list_of_inputs = [u, v, a, t, s]
    converted_inputs = []

    num_of_floats = 0

    for i in list_of_inputs:
        if i == '':
            converted_inputs.append(i)
        else:
            i = float(i)
            converted_inputs.append(i)
            num_of_floats+=1

    if num_of_floats < 3:
        print("not enough information to solve")
        return solve_uvats_with_user_input()

    # Assign values
    u = converted_inputs[0]
    v = converted_inputs[1]
    a = converted_inputs[2]
    t = converted_inputs[3]
    s = converted_inputs[4]

    # When a, t and s are known.
    if (u == '' and v == ''):
        nums = uv_zero(a, t, s)
        print(nums)
        return nums

    # When v, t and s are known
    elif (u == '' and a == ''):
        nums = ua_zero(v, t, s)
        print(nums)
        return nums
    
    # When a, v, and s are known
    elif (u == '' and t == ''):
        nums = ut_zero(a, v, s)
        print(nums)
        return nums
    
    # When b, a, and t are known
    elif (u == '' and s == ''):
        nums = us_zero(v, a, t)
        print(nums)
        return nums
    
    # When t, s, and u are known
    elif (v == '' and a == ''):
        nums = va_zero(t, s, u)
        print(nums)
        return nums

    # When u, a, and s are known
    elif (v == '' and t == ''):
        nums = vt_zero(u, a, s)
        print(nums)
        return nums
    
    # When u, a, and t are known
    elif (v == '' and s == ''):
        nums = vs_zero(u, a, t)
        print(nums)
        return nums

    # When u, v, and s are known
    elif (a == '' and t == ''):
        nums = at_zero(u, v, s)
        print(nums)
        return nums

    # When u, v, and t are known
    elif (a == '' and s == ''):
        nums = as_zero(u, v, t)
        print(nums)
        return nums

    # When u, v, and a are known
    elif (t == '' and s == ''):
        nums = ts_zero(u, v, a)
        print(nums)
        return nums

# solve_uvats_with_user_input()