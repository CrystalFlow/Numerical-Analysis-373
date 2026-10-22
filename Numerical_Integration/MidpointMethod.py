import sympy as sp

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


#Error Bound
def findMaxOf2ndDerivative(f, a, b):
    f_double_prime = sp.diff(f, t, 2)

    f_triple_prime = sp.diff(f_double_prime, t)
    critical_points = sp.solve(f_triple_prime, t)

    candidates = [pt for pt in critical_points if a <= pt <= b]
    candidates.append(a)
    candidates.append(b)

    max_y = max(f_double_prime.subs(t, pt) for pt in candidates)
    return max_y

if __name__ == "__main__":
    #Midpoint Method Integration
    print("Approximations: ")
    approximations = []
    for subinterval in N:
        sum = 0
        h = (b - a) / subinterval # Step Length

        for j in range(0, subinterval):
            x_j = a + (h * (j + 0.5)) # Midpoint of each interval

            sum += h * function.subs(t, x_j).evalf()

        approximations.append(sum)
        print(f"N = {subinterval}: I_{subinterval}(f) = {sum}")
    print()


    #Error
    print("Errors, | integral(f(x)) - I_n(f) |: ")
    error = []
    exact = sp.integrate(function, (t, a, b)).evalf()
    for index, subinterval in enumerate(N):
        error.append(abs(approximations[index] - exact))
        print(f"N = {subinterval}: Error = {error[index]}")
    print()


    #Error verification
    print("C/N^2, convergence, verification: ")
    for index, subinterval in enumerate(N):
        print(f"N = {subinterval}: C ≈ {error[index] * subinterval**2}")
    print()


    #Error Bound
    print("Error Bounds: ")
    error_bounds = []
    M = findMaxOf2ndDerivative(function, a, b).evalf()
    print(f"M value = {M}")
    for subinterval in N:
        bound = (M * (b-a)**3) / (24 * subinterval**2)
        error_bounds.append(bound)
        print(f"Error Bound, N = {subinterval}: {bound}")
