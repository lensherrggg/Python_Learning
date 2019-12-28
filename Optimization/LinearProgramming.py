import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

c=np.array([2,3,1])
A=np.array([[-1,-4,-2],[-3,-2,0]])
b=np.array([-8,-6])
bound=(0,None)
res=optimize.linprog(c,A_ub=A,b_ub=b,bounds=(bound,bound,bound))
print(res.x)
print(res.fun)