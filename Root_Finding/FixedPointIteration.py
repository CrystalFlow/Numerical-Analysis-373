import math
#Fixed point iteration method for finding roots

#Input your function before running
def function(x):
    return math.cos(x)

#Make an initial guess
p_0 = math.pi / 4
#Input your tolerance
tolerance = 0.01

def FPIteration(initP_i, tol): 
    print(f"Iteration 0: p_0 = {initP_i}")
    p_next = None
    counter = 0
    while True:
        p_next = function(initP_i)
        print(f"Iteration {counter + 1}: p_{counter + 1} = {p_next}")

        # if (abs(p_next - initP_i) < tol): break
        initP_i = p_next

        if (counter == 50): break
        counter += 1
    return p_next

ans = FPIteration(p_0, tolerance)
print(f"Root at x = {ans}, with tolerance of {tolerance}. ")