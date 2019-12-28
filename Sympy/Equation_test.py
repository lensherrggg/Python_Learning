from sympy import *
f=Function('f')
x=Symbol('x')
print(dsolve(diff(f(x),x,2)+f(x),f(x)))
a=Symbol('a')
print(solve(x-a,x))
y=Symbol('y')
print(solve([x+5*y-a,2*x-y+a],[x,y]))