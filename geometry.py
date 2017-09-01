# This program contains functions that evalutate formulas used in geometry.
#
# Brandon Hunter
# August 31, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print (triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def area_parrellelogram(b, h):
    a = b * h
    return a

def area_trapezoid(a, b, h):
    a = a + b / 2 * h
    return a

def vol_retangular(b, l, w):
    v = l * w * h
    return v

def vol_cone(r, h):
    v = math.pi * r ** 2 * h / 3
    return v

def vol_sphere(r):
    v = 4 / 3 * math.pi * r ** 3
    return v

def sa_rectangular(w, l, h):
    sa = w * l + h * l + h * w * 2
    return sa

def sa_sphere(r):
    sa = 4 * math.pi * r ** 2
    return sa

def hypotenuse(a, b):
    c = a ** 2 + b ** 2
    return c ** .5

