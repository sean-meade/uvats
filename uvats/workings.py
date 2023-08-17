import math
from .minus_b import minus_b


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


# When a, t and s are known.
def uv_zero(a, t, s):
    u = ((s - (0.5 * a * (t ** 2)))/t)

    v = math.sqrt( u ** 2 + 2 * a * s)

    return(u, v, a, t, s)

# When v, t and s are known
def ua_zero(v, t, s):
    u = ((s/(0.5 *t)) - v)

    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

# When a, v, and s are known
def ut_zero(a, v, s):
    t1, t2 = minus_b.minus_b((0.5 * a), (-v), s)
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
    
# When b, a, and t are known
def us_zero(v, a, t):
    u = v - (a * t)

    s = (u * t) + (0.5 * a * t**2)
    
    return(u, v, a, t, s)

# When t, s, and u are known
def va_zero(t, s, u):
    v = (s/(0.5 * t)) - u
    
    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

# When u, a, and s are known
def vt_zero(u, a, s):
    v = math.sqrt(u**2 + (2 * a * s))

    t = s/((0.5) * (u + v))

    return(u, v, a, t, s)

# When u, a, and t are known
def vs_zero(u, a, t):
    v = u + (a * t)

    s = (u * t) + (0.5 * a * t**2)

    return(u, v, a, t, s)

# When u, v, and s are known
def at_zero(u, v, s):
    a = (v**2 - u**2)/(2 * s)

    t = (v - u)/a

    return(u, v, a, t, s)

# When u, v, and t are known
def as_zero(u, v, t):
    s = 0.5 * (u + v) * t

    a = (v**2 - u**2)/(2 * s)

    return(u, v, a, t, s)

# When u, v, and a are known
def ts_zero(u, v, a):
    t = (v - u)/a

    s = 0.5 * (u + v) * t

    return(u, v, a, t, s)
