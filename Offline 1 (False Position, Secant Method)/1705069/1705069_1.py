import math as m
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

def mylog(x,itr,graph = False):
    '''
    This function uses the taylor series to approximate the value of ln(x+1)
    x = value of x
    itr = number of iterations
    graph = (default = False) if True, shows a plot of approx error vs number of iterations
    '''
    no_of_itr = []
    err = []
    
    result = 0
    for i in range(itr):
        prev = result
        result = result + ((-1)**i)*((x**(i+1))/(i+1))
        if graph == True:
            no_of_itr.append(i+1)
            err.append(abs((prev-result)/result)*100)
    
    if graph == True:
        no_of_itr = np.array(no_of_itr)
        err = np.array(err)
        figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
        plt.plot(no_of_itr,err)
        plt.xlabel("Number of iteration")
        plt.ylabel("Approximate error (%)")
        plt.title("Number of iteration vs approx error")
        plt.show()
    
    return result

x = float(input("Please enter x: "))
itr = int(input ("Please enter the number of iterations: "))

result = m.log(1+x)
result1 = mylog(x,itr,False)
error = (abs(result1 - result) / result)*100

print("From function: " + str(result))
print("From iteration: " + str(result1))
print("Error: " + str(error) + "%")

x = np.arange(-1+0.001,1,0.1)
y = np.log(x+1)
z = []
z1 = []
z2 = []
z3 = []
z4 = []

for i in x:
    z.append(mylog(i,1))
    z1.append(mylog(i,3))
    z2.append(mylog(i,5))
    z3.append(mylog(i,20))
    z4.append(mylog(i,50))

z = np.array(z)
z1 = np.array(z1)
z2 = np.array(z2)
z3 = np.array(z3)
z4 = np.array(z4)

figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.title("ln(x+1) curve using math.log(x) function")
plt.xlabel("x")
plt.ylabel("ln(x+1)")
plt.plot(x,y)

figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(x,y,x,z,x,z1,x,z2,x,z3,x,z4)
plt.xlabel("x")
plt.ylabel("Approximated values of ln(x+1)")
plt.gca().legend(('True value','1','3','5','20','50'))
plt.title("comparison between approximate values of ln(x+1) and math.log(x) function ")
plt.show()

mylog(0.5,50,True)