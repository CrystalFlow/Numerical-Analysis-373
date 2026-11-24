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
#Number of steps (h = 0.1)
N = [100, 1000, 10000]
#Exact solution y(t), used for the error calculation
exact_solution = 10 * sp.sqrt(2) * sp.tanh(t / sp.sqrt(2))


#Euler's Method
def EulersMethod(f, t_0, y_0, T, steps):
    h = (T - t_0) / steps # Step Length
    t_k = t_0
    y_k = y_0
    ts = [t_k]
    ys = [y_k]

    for k in range(steps):
        y_k = y_k + h * f.subs({t: t_k, y: y_k}).evalf() # y_{k+1} = y_k + h f(t_k, y_k)
        t_k = t_0 + (k + 1) * h
        ts.append(t_k)
        ys.append(y_k)

    return ts, ys

if __name__ == "__main__":
    print("Approximations: ")
    approximations = []
    for steps in N:
        ts, ys = EulersMethod(function, t_0, y_0, T, steps)
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
    print("C*h, convergence, verification (C = error / h): ")
    for index, steps in enumerate(N):
        h = (T - t_0) / steps
        print(f"N = {steps}, h = {h}: C ≈ {errors[index] / h}")
    print()

    #Step by step table for the first N: iteration, t_k, y_k, f(t_k, y_k)
    # print(f"Table, N = {N[0]}: ")
    # ts, ys = EulersMethod(function, t_0, y_0, T, N[0])
    # print(f"{'Iteration':<10}{'t_k':<10}{'y_k':<22}{'f(t_k, y_k)':<22}")
    # for k in range(len(ts)):
    #     f_k = function.subs({t: ts[k], y: ys[k]}).evalf()
    #     print(f"{k:<10}{float(ts[k]):<10.4f}{float(ys[k]):<22.10f}{float(f_k):<22.10f}")
