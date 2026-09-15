import sympy as sp
import math
# Newton's Method for finding roots of functions. Much faster and more efficient than Bisection.

t = sp.Symbol('t')
#Input function into 'f' for calculation before initializaiton. 
function = sp.sin(t) - 0.5                     # <-- 
#Differentiation of the input function.
func_prime = sp.diff(function, t)

#Input a guess x=x_0 to start the algorithm.
x = 1                                   # <-- 
#Input a tolerance 
tol = 0.01 #0.000001                              # <-- 

#To find the next iterate
def NewtonsProcess(x_Initial, tolerance, f, f_prime):
    #x_Initial may be real or complex. Casting to a native python complex at each step keeps the iterate a single
    #flat number rather than an ever-growing symbolic expression 
    counter = 0
    x_current = complex(x_Initial)
    x_next = x_current
    while True:
        f_val = complex(f.subs(t, x_current).evalf())
        f_prime_val = complex(f_prime.subs(t, x_current).evalf())
        x_next = x_current - f_val / f_prime_val
        if abs(x_next.imag) < 1e-12:
            x_next = x_next.real  #Display/return a plain real number once the imaginary part is negligible
        print(f"Iteration {counter + 1}: x_{counter + 1} = {x_next}")
        if abs(x_next - x_current) < tolerance: break
        x_current = x_next

        counter += 1
        if counter == 25: break
    return x_next

print(f"Guess 0: x_0 = {x}")
ans = NewtonsProcess(x, tol, function, func_prime)

print(f"Root at x = {ans}, with tolerance of {tol}. ")