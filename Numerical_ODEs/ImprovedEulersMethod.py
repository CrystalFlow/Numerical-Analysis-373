import sympy as sp

t = sp.Symbol('t')
y = sp.Symbol('y')

"""
User Inputs
"""
#f(t, y), right side of the ODE y' = f(t, y)
function = 10 - y**2 / 20
#Initial time
t_0 = 0
#Initial condition, y(t_0)
y_0 = 0
#Final time
T = 1
#Number of steps
N = [10, 100, 1000, 10000]
#Exact solution y(t), used for the error calculation
exact_solution = 10 * sp.sqrt(2) * sp.tanh(t / sp.sqrt(2))


#Improved Euler's Method (Heun's Method)
def ImprovedEulersMethod(f, t_0, y_0, T, steps):
    h = (T - t_0) / steps # Step Length
    t_k = t_0
    y_k = y_0
    ts = [t_k]
    ys = [y_k]

    for k in range(steps):
        t_next = t_0 + (k + 1) * h
        slope_1 = f.subs({t: t_k, y: y_k}).evalf()          # f(t_k, y_k)
        y_predict = y_k + h * slope_1                        # Euler predictor
        slope_2 = f.subs({t: t_next, y: y_predict}).evalf()  # f(t_{k+1}, predictor)
        y_k = y_k + (h / 2) * (slope_1 + slope_2)            # Average of the two slopes
        t_k = t_next
        ts.append(t_k)
        ys.append(y_k)

    return ts, ys

if __name__ == "__main__":
    print("Approximations: ")
    approximations = []
    for steps in N:
        ts, ys = ImprovedEulersMethod(function, t_0, y_0, T, steps)
        approximations.append(ys[-1])
        print(f"N = {steps}, h = {(T - t_0) / steps}: y({T}) ≈ {ys[-1]}")
    print()


    #Error
    print("Errors, | y(T) - y_N |: ")
    exact = exact_solution.subs(t, T).evalf()
    print(f"Exact calculation: {exact}")
    errors = []
    for index, steps in enumerate(N):
        error = abs(approximations[index] - exact)
        errors.append(error)
        print(f"N = {steps}: Error = {error}")
    print()


    #Error verification
    print("C*h^2, convergence, verification (C = error / h^2): ")
    for index, steps in enumerate(N):
        h = (T - t_0) / steps
        print(f"N = {steps}, h = {h}: C ≈ {errors[index] / h**2}")
    print()
