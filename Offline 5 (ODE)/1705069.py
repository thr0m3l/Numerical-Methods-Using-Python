import numpy as np
import matplotlib.pyplot as plt
import math

def dy1(x,y):
    return (x+20*y)*np.sin(x*y)

def dy2(x,y):
    return math.exp(x*y)*math.cos(x*y)

def euler(dy,x0,xn,y0,h):
    x = np.arange(x0,xn+h,h)
    y = np.zeros(len(x))
    y[0] = y0
    n = len(x) - 1
    for i in range(n):
      y[i+1] = y[i] + dy(x[i],y[i])*h
      
    return (x,y)

def heun(dy,x0,xn,y0,h):
    return rk2(dy,x0,xn,y0,h,1/2)

def ralston(dy,x0,xn,y0,h):
    return rk2(dy,x0,xn,y0,h,2/3)

def midpoint(dy,x0,xn,y0,h):
    return rk2(dy,x0,xn,y0,h,1)

def rk2(dy,x0,xn,y0,h,a2):
    x = np.arange(x0,xn+h,h)
    y = np.zeros(len(x))
    y[0] = y0
    n = len(x) - 1
    a1 = 1 - a2
    p1 = 1/(2*a2)
     
    for i in range(n):
        k1 = dy(x[i],y[i])
        k2 = dy(x[i] + h*p1, y[i] + p1*k1*h)
        y[i+1] = y[i] +  (a2*k2 + a1*k1)*h
    
    return (x,y)

def rk4(dy,x0,xn,y0,h):
    x = np.arange(x0,xn+h,h)
    y = np.zeros(len(x))
    y[0] = y0
    n = len(x) - 1
    for i in range(n):
        k1 = dy(x[i],y[i])
        k2 = dy(x[i] + 0.5*h, y[i] + 0.5*k1*h)
        k3 = dy(x[i] + 0.5*h, y[i] + 0.5*k2*h)
        k4 = dy(x[i] + h, y[i] + k3*h)
        y[i+1] = y[i] +  h*(k1 + 2*k2 + 2*k3 + k4) * (1/6)
    
    return (x,y)
def solve1(f,method,x0,xn,y0,h):
    
    title = ''
    
    if method == rk4:
        title = 'Runge Kutta 4th Order'
    elif method == heun:
        title = 'Heun Method'
    elif method == midpoint:
        title = 'Midpoint Method'
    elif method == ralston:
        title = 'Ralston Method'
    elif method == euler:
        title = 'Euler''s Method'
      
    plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
    plt.title(title)  
    plt.xlabel('values of x')
    plt.ylabel('values of y')
    for hi in h:
        x,y = method(f,x0,xn,y0,hi)
        plt.plot(x,y,label = '%.2f' %hi)
    plt.legend()
    plt.grid()
    plt.show()
    
def solve(f,x0,xn,y0,h):
    x1,y1 = rk4(f,x0,xn,y0,h)
    x2,y2 = euler(f,x0,xn,y0,h)
    x3,y3 = heun(f,x0,xn,y0,h)
    x4,y4 = ralston(f,x0,xn,y0,h)
    x5,y5 = midpoint(f,x0,xn,y0,h)
    plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
    plt.title('Step size = %.2f' %h)
    plt.xlabel('values of x')
    plt.ylabel('values of y')
    #plt.plot(x,y,'b',label = 'Analytic values',marker = '.')
    plt.plot(x1,y1, label = 'RK 4th Order')
    plt.plot(x2,y2,label = 'Euler''s Method')
    plt.plot(x3,y3,label = 'Heun Method')
    plt.plot(x4,y4,label = 'Ralston Method')
    plt.plot(x5,y5,label = 'Midpoint Method')
    
    plt.legend()
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    #solve(dy1,0,10,4,0.01)
    #solve(dy1,0,10,4,0.05)
    #solve(dy1,0,10,4,0.1)
    #solve(dy1,0,10,4,0.5)
    
    h = [0.01,0.05,0.1,0.5]
    #solve1(dy1,rk4,0,10,4,h)
    #solve1(dy1,euler,0,10,4,h)
    #solve1(dy1,heun,0,10,4,h)
    #solve1(dy1,midpoint,0,10,4,h)
    #solve1(dy1,ralston,0,10,4,h)
    
    solve(dy2,0,20,1,0.01)
    solve1(dy2,rk4,0,20,1,h)