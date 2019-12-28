import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy

def apply_ics(sol, ics, x, known_params):
    """
    Apply the initial conditions (ics), given as a dictionary on
    the form ics = {y(0): y0, y(x).diff(x).subs(x, 0): yp0, ...},
    to the solution of the ODE with independent variable x.
    The undetermined integration constants C1, C2, ... are extracted
    from the free symbols of the ODE solution, excluding symbols in
    the known_params list.
    """

    free_params = sol.free_symbols - set(known_params)
    eqs = [(sol.lhs.diff(x, n) - sol.rhs.diff(x, n)).subs(x, 0).subs(ics)
            for n in range(len(ics))]
    sol_params = sympy.solve(eqs, free_params)

    return sol.subs(sol_params)

sympy.init_printing()

t,k,T0,Ta=sympy.symbols('t,k,T_0,T_a')
T=sympy.Function('T')
ode=T(t).diff(t)+k*(T(t)-Ta)

ode_sol=sympy.dsolve(ode)

print(ode)
print(ode_sol)
print(ode_sol.lhs,'=',ode_sol.rhs)

ics={T(0):T0}
C_eq=sympy.Eq(ode_sol.lhs.subs(ics),ode_sol.rhs.subs(t,0))
print(C_eq)

C_sol=sympy.solve(C_eq)
print(ode_sol.subs(C_sol[0]))

print(apply_ics(ode_sol,ics,t,[k,Ta]))