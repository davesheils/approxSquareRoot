def sqrt(x):
    # adapted from https://tour.golang.org/flowcontrol/8
    # initial guess
    z = 1.0
    # keep getting a better estimate for square 
    # root of x until you are within 2 decimal places
    
    while abs(z*z - x) > 0.01:
        # get better approx for sqrt
        z -= (z*z - x) / (2*z)
    return z


# Calculate sqrt of 8
x = float(input("enter number"))
print(sqrt(x))
print(sqrt(x)**2)