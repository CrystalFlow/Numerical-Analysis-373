#This file will implement polynomial root finding using the Mueler's Method, with either 
# Newton's Method or Quadratic Interpolation
import math
import sympy as sp
from NewtonsMethod import NewtonsProcess

t = sp.Symbol('t')
#Input function into 'f' for calculation before initializaiton.
f = t**4 - 5*t**3 + 9*t**2 - 53*t +132             # <--
#Calculating the the first differential
f_prime = sp.diff(f, t)
#Input the tolerance needed
tolerance = 0.0001                        # <--
#Input the initial x guess for the first Newton's Method process.
#A tiny imaginary part is included so Newton's Method (now complex-capable, see NewtonsMethod.py)
#can also converge onto complex-conjugate root pairs, not just real roots.
x = 0.5 + 0.1j                            # <--

listOfFunctions = [f]
roots = []

#Polish: a root found on a deflated (and thus slightly inaccurate) polynomial is refined by using it
#as the initial guess for Newton's Method on the ORIGINAL function, correcting accumulated deflation error.
def polish_root(root_guess):
    polished = NewtonsProcess(root_guess, tolerance, f, f_prime)
    print(f"Polished root: {root_guess} -> {polished}")
    return polished

x_initial = NewtonsProcess(x, tolerance, f, f_prime)
x_initial = polish_root(x_initial)
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

    current_root = polish_root(current_root)
    roots.append(current_root)
    print(f"Root {len(roots)} found: t = {current_root}")

print(f"\nAll roots found: {roots}")
print(f"Polynomials used at each deflation stage: {listOfFunctions}")