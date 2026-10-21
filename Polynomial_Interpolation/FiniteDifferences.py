# Only made this for homework for now 
# This finds the approximated value of the second derivative using the finite differences method
import sympy as sp

t = sp.Symbol('t')

function = sp.exp('t')
x_initial = 2.0
h_vals = [0.1, 0.01, 10**-3, 10**-4, 10**-5, 10**-6, 10**-7]

def d2(f, x_0, h):
    d2Approx = ( f.subs(t, x_0 + h).evalf() - (2 * f.subs(t, x_0).evalf()) + f.subs(t, x_0 - h).evalf() ) / (h**2)
    return d2Approx

evaluated_val = sp.diff(function, t, 2).subs(t, x_initial).evalf()

approx = []
error = []
for i in range(len(h_vals)):
    approx.append(d2(function, x_initial, h_vals[i]))
    error.append(sp.Abs(evaluated_val - approx[i]))


print(f"Actual value {evaluated_val}")
print(f"Approximated: {approx}")
print(f"Error |f\"({x_initial}) - D_2(h)| = {error}")