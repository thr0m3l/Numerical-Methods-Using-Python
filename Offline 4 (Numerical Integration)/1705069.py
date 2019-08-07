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
    intv1 = abs(x[1] - x[0])
    begin = 0
    end = 1
    
    for i in range(1,n+1):
        intv2 = abs(x[i] - x[i-1])
        
        if not isclose(intv2,intv1,abs_tol = 0.00001) or i - begin >= 4 or i == n:
            if i == n:
                end = i+1
            else:
                end = i
            
            x1 = x[begin:end]
            y1 = y[begin:end]
            
            if end - begin == 2:
                ans += trapezoidal(x1,y1)
                plt.fill_between(x1,y1,color='#702239',label ='Trapezoidal Rule')
                trap += 1
            elif end - begin == 3:
                ans += simpson13(x1,y1)
                plt.fill_between(x1,y1,color='#227049',label = 'Simpson''s 1/3 Rule')
                simp13 += 2
            elif end - begin == 4:
                ans += simpson38(x1,y1)
                plt.fill_between(x1,y1,color='#2d2270',label = 'Simpson''s 3/8 Rule')
                simp38 += 3
            #print('%.2f %.2f %.3f' %(x[begin],x[end-1],ans))
            plt.legend(loc = 'best')
            begin = end - 1
        intv1 = intv2
        
        
    print('Trapezoidal rule : %d intervals' %trap)
    print('1/3 rule : %d intervals' %simp13)
    print('3/8 rule: %d intervals' %simp38)
    print('Value of the integral : %.4f' %ans)
    
if __name__ == '__main__':
    x,y = read_file('input.txt')  
    integral(x,y)
    
    