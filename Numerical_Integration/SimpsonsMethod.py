import sympy as sp

t = sp.Symbol('t')

"""
User Inputs
"""
#f(x), function
function = t**2 + sp.cos(t)
#Subintervals (must be even for Simpson's Method)
N = [10, 100, 1000]
#Left Bound
a = 0
#Right Bound
b = 3


#Simpson's Method Integration
print("Approximations: ")
approximations = []
for subinterval in N:
    sum = 0
    h = (b - a) / subinterval # Step Length
    pre_sum = (h / 3) * (function.subs(t, a).evalf() + function.subs(t, b).evalf())

    for i in range(1, subinterval):
        x_j = a + i * h

        if i % 2 == 1:
            sum += (4 * h / 3) * function.subs(t, x_j).evalf() # Odd nodes, weight 4
        else:
            sum += (2 * h / 3) * function.subs(t, x_j).evalf() # Even interior nodes, weight 2

    total_approx = pre_sum + sum
    approximations.append(total_approx)
    print(f"N = {subinterval}: I_{subinterval}(f) = {total_approx}")
print()


#Error
print("Errors, | integral(f(x)) - S_n(f) |: ")
error = []
exact = sp.integrate(function, (t, a, b)).evalf()
for index, subinterval in enumerate(N):
    error.append(abs(approximations[index] - exact))
    print(f"N = {subinterval}: Error = {error[index]}")
print()


#Error verification
print("C/N^4, convergence, verification: ")
for index, subinterval in enumerate(N):
    print(f"N = {subinterval}: C ≈ {error[index] * subinterval**4}")
print()


#Error Bound
print("Error Bounds: ")
def findMaxOf4thDerivative(f, a, b):
    f_fourth = sp.diff(f, t, 4)

    f_fifth = sp.diff(f_fourth, t)
    critical_points = sp.solve(f_fifth, t)

    candidates = [pt for pt in critical_points if a <= pt <= b]
    candidates.append(a)
    candidates.append(b)

    max_y = max(abs(f_fourth.subs(t, pt)) for pt in candidates)
    return max_y

error_bounds = []
M = findMaxOf4thDerivative(function, a, b).evalf()
print(f"M value = {M}")
for subinterval in N:
    bound = (M * (b-a)**5) / (2880 * subinterval**4)
    error_bounds.append(bound)
    print(f"Error Bound, N = {subinterval}: {bound}")
