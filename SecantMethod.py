import math
# The Secant Method for finding roots of functions. Slightly faster and does not require derivation, but is a pain sometimes. 

#Initial guesses (do not need to bracket a solution)
x0 = 1
x1 = 0.8
#Insert tolerance value
tolerance = 0.01

#Input function for calculation before initializaiton. 
def function(x):
    return math.sin(x) - 0.5

def SecantProcess(x0, x1, tol):
    counter = 0
    x2 = None

    while True: 
        x2 = ( (x0 * function(x1)) - (x1 * function(x0)) ) / ( function(x1) - function(x0) )
        print(f"Iteration: {counter}, iterate: {x2}")
        x0 = x1
        x1 = x2

        if abs(x1 - x0) < tol: break

        counter += 1
        if counter == 25: break
    return x2

ans = SecantProcess(x0, x1, tolerance)
print(f"Root at x = {ans}, with tolerance of {tolerance}. ")