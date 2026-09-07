import math
# The bisection method to find roots of functions given a bracket. 

# Iterations needed for Bisection to find root, given a tolerance
def iterationsNeeded (tolerance, currentBracket):
    iteration = math.ceil( (math.log((currentBracket[1] - currentBracket[0]) / tolerance) / math.log(2) ) - 1 )
    #Might need to add to account for division issues
    return iteration

def bisectionProcess(tolerance, currentBracket):
    k = iterationsNeeded(tolerance, currentBracket)
    print(f"Iterations needed: {k}")
    print("Brackets: ")
    c = None
    for i in range(k):
        c = (currentBracket[1] + currentBracket[0]) / 2
        val = function(c)
        if val > 0:   currentBracket[1] = c
        elif val < 0: currentBracket[0] = c
        else:         return c                  # Because the root is found
        print(f"({currentBracket[0]}, {currentBracket[1]})")
    return c

#Input function for calculation before initializaiton. 
def function(x):
    return math.sin(x) - 0.5

#Insert values that bracket a solution/root before initialization. 
currBracket = [0, 1]
tol = 0.01
ans = bisectionProcess(tol, currBracket)
print(f"Root at x = {ans}, with tolerance of {tol}.")