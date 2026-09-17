#This file reconstructs a polynomial p(x) from given points using Lagrangian Interpolation.
import sympy as sp

x = sp.Symbol('x')

#Input the # of points (x_k, y_k) the polynomial passes through - type them directly into this array.
points = [(1, sp.ln(1)), (1.2, sp.ln(1.2)), (1.5, sp.ln(1.5)), (2, sp.ln(2))]          # <--

def LagrangeBasis(points, k):
    x_k = points[k][0]
    L_k = 1
    for j in range(len(points)):
        if j != k:
            x_j = points[j][0]
            L_k *= (x - x_j) / (x_k - x_j)
    return L_k

def QuadraticInterpolation(points):
    p = 0
    for k in range(len(points)):
        L_k = LagrangeBasis(points, k)
        print(f"L_{k}(x) = {L_k}")
        y_k = points[k][1]
        p += y_k * L_k
    p = sp.expand(p)
    print(f"p(x) = {p}")
    return p

p_x = QuadraticInterpolation(points)
coefficients = sp.Poly(p_x, x).all_coeffs()
print(f"a = {coefficients[0]}, b = {coefficients[1]}, c = {coefficients[2]}, d = {coefficients[3]}")

error = []
for i in range(len(points)):
    error.append(abs(sp.ln(points[i][0] - p_x.subs(x, points[i][0]) )))
print(error)