#import sympy
from sympy.abc import x,y

aa=solve([x-200*y,
          (100/3*y)**2+(100/3/400*x)**2-0.01],[x,y])
print(aa)