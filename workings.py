import math
import minusB
"""
u = initial velocity
v = final velocity
a = acceleration
t = time
s = displacment

t u - a v s

v = ut + 0.5(a)t**
v** = u** + 2as
s = ut + 0.5(a)t**
s = vt - 0.5(a)t**
s = 0.5(u + v)t

u = 10
v = 100
a = 6.0606
t = 16.5
s = 990
"""

def uvZero(a, t, s):
    u = ((s - (0.5 * a * (t ** 2)))/t)

    v = math.sqrt( u ** 2 + 2 * a * s)

    return(u, v, a, t, s)

def uaZero(v, t, s):
    u = ((s/(0.5 *t)) - v)

    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

def utZero(a, v, s):
    t1, t2 = minusB.minusB((0.5 * a), (-v), s)
    t, u = 0, 0
    if t1 > 0:
        vel = (s - (0.5 * a * (t1 ** 2)))/t1
        if vel > 0:
            u = vel
            t = t1

    elif t2 > 0:
        vel = (s - (0.5 * a * (t2 ** 2)))/t2
        if vel > 0:
            u = vel
            t = t2
    return(u, v, a, t, s)
    

def usZero(v, a, t):
    u = v - (a * t)

    s = (u * t) + (0.5 * a * t**2)
    
    return(u, v, a, t, s)

def vaZero(t, s, u):
    v = (s/(0.5 * t)) - u
    
    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

def vtZero(u, a, s):
    v = math.sqrt(u**2 + (2 * a * s))

    t = s/((0.5) * (u + v))

    return(u, v, a, t, s)

def vsZero(u, a, t):
    v = u + (a * t)

    s = (u * t) + (0.5 * a * t**2)

    return(u, v, a, t, s)

def atZero(u, v, s):
    a = (v**2 - u**2)/(2 * s)

    t = (v - u)/a

    return(u, v, a, t, s)

def asZero(u, v, t):
    s = 0.5 * (u + v) * t

    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

def tsZero(u, v, a):
    t = (v - u)/a

    s = 0.5 * (u + v) * t

    return(u, v, a, t, s)
