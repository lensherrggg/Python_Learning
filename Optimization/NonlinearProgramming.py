from scipy import optimize
import numpy as np

def fun(args):
    a=args
    v=lambda x:a/x[0]+x[0]
    return v
if __name__=="__main__":
    args=(1)
    x0=np.asarray((2))
res=optimize.minimize(f,x0,method='SLSQP')
print(res.x)
print(res.fun)