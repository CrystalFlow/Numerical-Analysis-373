#This file will implement polynomial root finding using the Mueler's Method, with either 
# Newton's Method or Quadratic Interpolation
import math
import sympy as sp
from NewtonsMethod import NewtonsProcess

t = sp.Symbol('t')
#Input function into 'f' for calculation before initializaiton.
f = t**3 - 6*t**2 + 11*t - 6             # <--
#Calculating the the first differential
f_prime = sp.diff(f, t)
#Input the tolerance needed
tolerance = 0.01                        # <--
#Input the initial x guess for the first Newton's Method process
x = 0                                   # <--

listOfFunctions = [f]
roots = []

x_initial = NewtonsProcess(x, tolerance, f, f_prime)
roots.append(x_initial)
print(f"Root 1 found: t = {x_initial}")

current_f = f
current_root = x_initial

while sp.degree(current_f, t) > 1:
    #Polynomial division: divide out the (t - root) factor found so far, discarding the (approximate) remainder
    quotient, remainder = sp.div(current_f, t - current_root, t)
    current_f = sp.expand(quotient)
    listOfFunctions.append(current_f)
    print(f"Deflated polynomial: {current_f}")

    if sp.degree(current_f, t) == 1:
        #Linear factor left over: solve a*t + b = 0 directly instead of running Newton's method on it
        a, b = sp.Poly(current_f, t).all_coeffs()
        current_root = -b / a
    else:
        current_f_prime = sp.diff(current_f, t)
        current_root = NewtonsProcess(x, tolerance, current_f, current_f_prime)

    roots.append(current_root)
    print(f"Root {len(roots)} found: t = {current_root}")

print(f"\nAll roots found: {roots}")
print(f"Polynomials used at each deflation stage: {listOfFunctions}")