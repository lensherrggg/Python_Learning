from sympy import *
from sympy.abc import x,y
aa=solve([2770*x-y,y**2+(277*x)**2-277**2-2.4**2],[x,y])
print(aa)