import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


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
    h = (x[n] - x[0])/(n)
    s = 0.5*(y[0] + y[n])
    
    for i in range(1,n):
        s += y[i]
    
    return s*h
    
def simpson13(x,y):
    n = len(x) - 1
    
    if n < 2:
        return 0
    
    h = (x[n] - x[0])/n
    s = (y[0] + y[n])
    
    for i in range(1,n,2):
        s+= 4*y[i]
    for i in range(2,n,2):
        s+= 2*y[i]
    
    return h/3 * s

def simpson38(x,y):
    n = len(x) - 1
    
    if n < 3:
        return 0
    
    h = (x[n] - x[0])/n
    s = (y[n] + y[0])
    for i in range(1,n,3):
        s+= 3*(y[i] + y[i+1])
    for i in range(3,n,3):
        s+= 2*y[i]
    
    return 3*h/8* s

def integral(x,y):
    '''
    Parameters:
        x = values of input x
        y = values of output f(x) 
    '''
    
    #Shows the plot
    plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Values of x')
    plt.ylabel('Values of y')
    plt.plot(x,y,marker = '.', color = 'k') 
    plt.title("Numerical Integration")
    plt.grid()
    
    #Detects equal intervals and divides them accordingly
    n = len(x) - 1
    ans = trap = simp13 = simp38 = begin = 0
    intv1 = abs(x[1] - x[0])
    i = end = 1
    while i < n + 1:
        intv2 = abs(x[i] - x[i-1])
        if abs(intv2 - intv1) > 0.0000000001 or i == n:
            
            if i == n and abs(intv2 - intv1) > 0.0000000001:
                end = i
                i -= 1
            elif i == n:
                end = i + 1
            else:
                end = i
            
            x1 = x[begin:end]
            y1 = y[begin:end]
            
            diff = end - begin - 1
            
            if diff == 1:
                ans += trapezoidal(x1,y1)
                plt.fill_between(x1,y1,color='#702239')
                trap += 1
            elif diff % 3 == 0:
                #All simp 3/8
                ans += simpson38(x1,y1)
                plt.fill_between(x1,y1,color='#2d2270')
                simp38 += diff
            elif diff % 3 == 1:
                #Does 2 Simp 1/3 + Rest Simp 3/8
                tempx1 = x1[0:5]
                tempy1 = y1[0:5]
                tempx2 = x1[4:diff+1]
                tempy2 = y1[4:diff+1]
                ans += simpson38(tempx2,tempy2)
                ans += simpson13(tempx1,tempy1)
                plt.fill_between(tempx1,tempy1,color='#227049')
                plt.fill_between(tempx2,tempy2,color='#2d2270')
                simp38 += diff - 4
                simp13 += 4
            elif diff % 3 == 2:
                #Does 1 Simp 1/3 + Rest Simp 3/8
                tempx1 = x1[0:3]
                tempy1 = y1[0:3]
                tempx2 = x1[2:diff+1]
                tempy2 = y1[2:diff+1]
                ans += simpson38(tempx2,tempy2)
                ans += simpson13(tempx1,tempy1)
                plt.fill_between(tempx1,tempy1,color='#227049')
                plt.fill_between(tempx2,tempy2,color='#2d2270')
                simp38+= diff - 2
                simp13+= 2
            #print('From : %.2f to: %.2f ans: %.3f intervals: %d' %(x[begin],x[end-1],ans,diff))
            begin = end - 1
        intv1 = intv2
        i += 1
        l0 = mpatches.Patch(color = 'k', label = 'Data Points' )
        l1 = mpatches.Patch(color='#227049', label='Simpson''s 1/3 Rule')
        l2 = mpatches.Patch(color='#2d2270', label='Simpson''s 3/8 Rule')
        l3 = mpatches.Patch(color='#702239', label='Trapezoidal Rule')
        plt.legend(handles=[l0,l1,l2,l3],loc = 'best')
        
    print('Trapezoidal: %d intervals' %trap)
    print('1/3 rule: %d intervals' %simp13)
    print('3/8 rule: %d intervals' %simp38)
    print('\nIntegral value: %.5f' %ans)    
    
if __name__ == '__main__':
    x,y = read_file('data.txt')  
    integral(x,y)