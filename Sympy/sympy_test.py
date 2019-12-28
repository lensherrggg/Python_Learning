from sympy import *
x=Symbol('x')
print(apart(1/((x+2)*(x+1)),x))
print(together((1/(x+1)-1/(x+2)),x))
print(cos(x).series(x,0,10))
print(integrate(sin(x),x))
print(integrate(x**2,(x,-1,1)))
