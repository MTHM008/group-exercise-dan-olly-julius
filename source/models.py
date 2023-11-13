import numpy as np

#This is a function that computes the SIR model right hand side
def SIR(Y, r, a):
    S, I, _ = Y
    return [-r*I*S,r*I*S - a*I, a*I]


#The Brusselator function takes a 2D array Y and applies the brusselator function
def Brusselator(Y, a, b):
    x, y = Y
    return np.array([a + x**2*y - b*x +x, b*x - x**2*y])
