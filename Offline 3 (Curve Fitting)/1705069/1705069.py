import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

def read_file(filename):
    
    file = open(filename,"r")
    
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
    x = np.array(x)
    y = np.array(y)
    return (x,y)

def poly_reg(x,y,order):
    A = np.zeros((order+1,order+1))
    B = np.zeros(order+1)
    a = np.zeros(order+1)
    
    m = len(x)
    for row in range(order+1):
        for col in range(order+1):
            if row == 0 and col == 0:
                A[row,col] = m
                continue
            A[row,col] = np.sum(x**(row+col))
        B[row] = np.sum(x**row * y)
    a = np.linalg.solve(A,B)
    
    mean = np.mean(y)
    yerr = np.sum((y-mean)**2)
    
    sumsum = 0
    for j,yi in enumerate(y):
        sum = yi
        for i,ai in enumerate(a):
            sum -= ai*x[j]**i
        sum = sum**2
        sumsum += sum
    reg_coeff = sqrt((yerr-sumsum)/yerr)
    
    return (a,reg_coeff)

def soln_to_plot(x, result, color, lbl):
    y = np.zeros(len(x))
    for i,xi in enumerate(result):
        y += xi * x ** i
    
    plt.plot(x,y,color,label = lbl)
if __name__ == '__main__':
    
    x,y = read_file('data.txt')
    
    plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
    plt.scatter(x,y, color = 'c', s = 5)
    plt.xlabel('x')
    plt.ylabel('y')

    x1 = np.arange(np.min(x),np.max(x),0.1)
    
    res1,rc1 = poly_reg(x,y,1)    
    res2,rc2 = poly_reg(x,y,2)
    res3,rc3 = poly_reg(x,y,3)
    
    soln_to_plot(x1,res1,'k', 'First order')
    soln_to_plot(x1,res2,'r', 'Second order')
    soln_to_plot(x1,res3,'m','Third order')
    plt.legend()
    #plt.show()
    
    print("Regression co-efficients & parameters: \n")
    print("For 1st order: ")
    print(res1)
    print('r = %f\n' %rc1)
    print("For 2nd order: ")
    print(res2)
    print('r = %f\n' %rc2)
    print("For 3rd order: ")
    print(res3)
    print('r = %f \n' %rc3)