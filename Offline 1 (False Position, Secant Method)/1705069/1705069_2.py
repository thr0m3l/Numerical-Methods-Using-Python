import numpy as np
from matplotlib import pyplot as plt
from math import sqrt
from matplotlib.pyplot import figure

def F(x):
    return (x/(1-x))*(sqrt(6/(2+x))) - 0.05

def graph(func, init, end, incr):
    print ("-- Graphical Method --")
    x = np.arange(init,end,incr)
    y = []
    for i in x:
        y.append(func(i))
    
    y = np.array(y)

    markers_on = []
    ans = 0
    for i in range(len(y)):
        if round(y[i],3) == 0:
            markers_on.append(i)
            ans = x[i]
        
    figure(num=None, figsize=(8, 10), dpi=80, facecolor='w', edgecolor='k')        
    plt.plot(x, y, '-bD', markevery=markers_on)
    plt.grid(True)
    plt.show()
    print("Root found by graphical method:  " + str(ans))
    print("----------------")
        
def secant(func,g1,g2,exp_err,max_itr):
    print ("-- Secant Method --")
    i = 0
    if func(g1)*func(g2) >= 0:
        print("Secant method failed")
        return None
    x1 = g1
    x2 = g2
    
    err = exp_err + 1
    while i<max_itr and err > exp_err:
        x = x1
        x1 = x2
        x2 = x1 - ((x-x1)/(func(x)-func(x1)))*func(x1)
        err = abs((x2-x1)/x2)*100
        i = i + 1
        
    print ("Root: " + str(x1))
    print("Number of iterations: " + str(i))
    print ("Error: " + str(err) + "%")
    print ("------------------------------")
    
def false_pos(func,xl,xu,exp_err,max_itr):
    print ("-- False position method --")
    i = 0
    xr = 1000
    err = exp_err + 1
    
    while i < max_itr and err > exp_err:
        prev = xr
        xr = xu - (func(xu)*(xl - xu))/(func(xl) - func(xu))
        if func(xl)*func(xr) < 0:
            xu = xr
        elif func(xl)*func(xr) > 0:
            xl = xr
        else :
            break
        err = abs((prev-xr)/xr)*100
        i = i + 1
        
    print ("Root: " + str(xr))
    print("Number of iterations: " + str(i))
    print ("Error: " + str(err) + "%")
    print ("------------------------------")
        
#Main:
graph(F,-0.5,0.85,0.001)
false_pos(F,0,0.5,0,1000)
secant(F,0,0.5,0,1000)
