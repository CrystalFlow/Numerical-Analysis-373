import numpy as np

# 1. Define the 3x3 coefficient matrix (A)
A = np.array([
    [1,  1, 1],
    [1,  0.25,  0.0625],
    [1,  0.0625, 0.00390625]
])

# 2. Define the constant vector (b)
b = np.array([0.6839397206, 0.6452351901, 0.635409429])

# 3. Solve for x (Ax = b)
x = np.linalg.solve(A, b)

print("Solution vector x:")
print(x)