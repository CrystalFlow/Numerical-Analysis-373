#This file reconstructs a quadratic p(x) = ax^2 + bx + c from 3 given points using Lagrangian Interpolation.
import sympy as sp

x = sp.Symbol('x')

#Input the 3 points (x_k, y_k) the polynomial passes through - type them directly into this array.
points = [(0, 1), (1, 2), (2, 1)]          # <--

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
a, b, c = sp.Poly(p_x, x).all_coeffs()
print(f"a = {a}, b = {b}, c = {c}")
