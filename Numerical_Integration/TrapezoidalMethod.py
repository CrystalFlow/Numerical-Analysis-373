import sympy as sp
from MidpointMethod import findMaxOf2ndDerivative

t = sp.Symbol('t')

"""
User Inputs
"""
#f(x), function
function = t**2 + sp.cos(t)
#Subintervals
N = [10, 100, 1000]
#Left Bound
a = 0
#Right Bound
b = 3


#Trapezoidal Method Integration
approximations = []
for subinterval in N:
    sum = 0
    h = (b - a) / subinterval # Step Length
    pre_sum = 0.5 * h * (function.subs(t, a).evalf() + function.subs(t, b).evalf())

    for i in range(1, subinterval):
        x_j = a + i * h

        sum += h * function.subs(t, x_j).evalf()

    total_approx = pre_sum + sum
    approximations.append(total_approx)
    print(f"N = {subinterval}: I_{subinterval}(f) = {total_approx}")
print()


#Error
error = []
exact = sp.integrate(function, (t, a, b)).evalf()
for index, subinterval in enumerate(N):
    error.append(abs(approximations[index] - exact))
    print(f"N = {subinterval}: Error = {error[index]}")
print()


#Error Bound 
error_bounds = []
M = findMaxOf2ndDerivative(function, a, b).evalf()
for subinterval in N:
    bound = (M * (b-a)**3) / (12 * subinterval**2)
    error_bounds.append(bound)
    print(f"Error Bound: {bound}")