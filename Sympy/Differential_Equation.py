from sympy import *
f=Function('f')
x=Symbol('x')
a=Symbol('a')
b=Symbol('b')
print(dsolve(diff(f(x),x,2)+a*f(x)-b,f(x)))