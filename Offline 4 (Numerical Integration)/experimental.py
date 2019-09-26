import numpy as np
from matplotlib import pyplot as plt
from math import isclose


def read_file(filename):
    
    file = open(filename,"r")
    n = file.readline()
    n = int(n)
    lines = file.readlines()
    data = []
    for line in lines:
        data += [float(x) for x in line.split()]           
    x = []
    y = []
    for i,xi in enumerate(data):
        if i % 2 == 0 :
            x.append(xi)
        else : 
            y.append(xi)
    return (np.array(x),np.array(y))

def trapezoidal(x,y):
    n = len(x) - 1
    h = (x[n]-x[0])/(n)
    s = 0.5*(y[0] + y[n])
    
    for i in range(1,n):
        s += y[i]
    
    return s*h
    
def simpson13(x,y):
    n = len(x) - 1
    h = (x[n]-x[0])/n
    s = (y[0] + y[n])
    
    for i in range(1,n,2):
        s+= 4*y[i]
    for i in range(2,n,2):
        s+= 2*y[i]
    
    return h/3 * s

def simpson38(x,y):
    n = len(x) - 1
    h = (x[n]-x[0])/n
    s = (y[n] + y[0])
    for i in range(1,n,3):
        s+= 3*(y[i] + y[i+1])
    for i in range(3,n,3):
        s+= 2*y[i]
    
    return 3*h/8* s

def integral(x,y):
    #Shows the plot
    plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Values of x')
    plt.ylabel('Values of y')
    plt.plot(x,y,marker = 'o', color = 'k') 
    plt.title("Numerical Integration")
    plt.grid()
    
    #Detects equal intervals and divides them accordingly
    n = len(x) - 1
    ans = trap = simp13 = simp38 = 0
    h = abs(x[1] - x[0])
    k = 1
    
    for j in range(1,n):
        hf = x[j+1]-x[j]
        
        if abs(h-hf) < 0.00001:
            if k == 3:
                ans += simpson13(x[j-3:j],y[j-3:j])
                k -= 1
            else:
                k += 1
        else:
            if k == 1:
                ans += trapezoidal(x[j-1:j+1],y[j-1:j+1])
            elif k == 2:
                ans += simpson13(x[j-2:j+1],y[j-2:j+1])
            else:
                ans += simpson38(x[j-3:j+1],y[j-3:j+1])
            
            k = 1
        h = hf
    print('Trapezoidal: %d intervals' %trap)
    print('1/3 rule: %d intervals' %simp13)
    print('3/8 rule: %d intervals' %simp38)
    print('\nIntegral value: %.5f' %ans)    

if __name__ == '__main__':
    x,y = read_file('input.txt')  
    integral(x,y)
    
    