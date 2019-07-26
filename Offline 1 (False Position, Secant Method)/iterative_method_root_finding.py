from math import sqrt
x = 1 #Initial value


for i in range(1,10001):
    xnew = (0.05*(1-x))/(sqrt(6/(2+x)))
    #if abs(xnew - x) < 0.000000001 :
    if x == xnew:
        break
    x = xnew

print("The root: %.15f" %xnew)
print("The number of iterations: %d" %i)