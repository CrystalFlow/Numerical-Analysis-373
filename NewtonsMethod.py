import sympy as sp
import math
from math import inf
# Newton's Method for finding roots of functions. Much faster and more efficient than Bisection. 

t = sp.Symbol('t')
#Input function into 'f' for calculation before initializaiton. 
f = sp.sin(t) - 0.5                     # <-- 
#Differentiation of the input function.
f_prime = sp.diff(f, t)

#Input a guess x=x_0 to start the algorithm.
x = 1                                   # <-- 
#Input a tolerance 
tol = 0.01 #0.000001                              # <-- 

#To find the next iterate
def NewtonsProcess(x_Initial, tolerance): 
    counter = 0
    x_next = inf 
    while True:
        x_next = x_Initial - (f.subs(t, x_Initial).evalf() / f_prime.subs(t, x_Initial).evalf() )
        print(f"Iteration {counter + 1}: x_{counter + 1} = {x_next}")
        if abs(x_next - x_Initial) < tol: break
        x_Initial=x_next

        counter += 1
        if counter == 25: break
    return x_next

print(f"Guess 0: x_0 = {x}")
ans = NewtonsProcess(x, tol)

print(f"Root at x = {ans}, with tolerance of {tol}. ")