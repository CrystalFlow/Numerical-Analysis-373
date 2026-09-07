import math
# The bisection method to find roots of functions given a bracket. 


#Input function for calculation before initializaiton. 
def function(x):
    return math.sin(x) - 0.5

#Insert values that bracket a solution/root before initialization. 
currentBracket = [0, 1]

# Iterations needed for Bisection to find root, given a tolerance
def iterationsNeeded (tolerance, currentBracket) -> int:
    iteration = int( (math.log((currentBracket[1] - currentBracket[0]) / tolerance) / math.log(2) ) - 1 )
    #Might need to add to account for division issues

def bisectionProcess(currentBracket, tolerance):
    k = iterationsNeeded(tolerance, currentBracket)
    c = None
    for i in range(k):
        c = (currentBracket[1] + currentBracket[0]) / 2
        val = function(c)
        if val > 0:   currentBracket[1] = c
        elif val < 0: currentBracket[0] = c
        else:         return c                  # Because the root is found
    return c