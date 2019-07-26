import numpy as np



def decompose(a,n):
    l = np.zeros((n,n))
    np.fill_diagonal(l, 1)
    u = np.copy(a)
    for k in range(n-1):
        for i in range(k+1,n):
            factor = u[i,k]/u[k,k]
            l[i,k] = factor
            for j in range(k,n):
                u[i,j] = u[i,j] - factor*u[k,j]
    
    return (l,u)

def subsitution(n,b,l,u):
    d = np.zeros(n)
    x = np.zeros(n)
    #Forward Subsitution
    d[0] = b[0]/l[0,0]
    for i in range(1,n):
        sum = b[i]
        for j in range(i):
            sum = sum - l[i,j]*d[j]
        d[i] = sum
    
    
    #Back subsitution
    x[n-1] = d[n-1]/u[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum = sum + u[i,j]*x[j]
        x[i] = (d[i]-sum)/u[i,i]
    
    return (d,x)

def lu_decomposition(a,b):
    n = len(b)
    
    l,u = decompose(a,n)
    
    #Checks if all numbers in a row in U Matrix == 0
    all_zero = False
    for i in range(n):
        all_zero = True
        for j in range(n):
            if u[i,j] != 0:
                all_zero = False
                break
        if all_zero == True:
            break
    
    if all_zero == True:
        print("No unique solution")
        file= open('out1.txt','w')
        file.write("No unique solution")
        exit()
    
    else :
        d,x = subsitution(n,b,l,u)
        file= open('out1.txt','w')
        np.savetxt(file, l, fmt='%.4f', delimiter = ' ' )
        file.write("\n")
        np.savetxt(file, u, fmt='%.4f', delimiter = ' ' )
        file.write("\n")
        np.savetxt(file, d, fmt='%.4f', delimiter = ' ' )
        file.write("\n")
        np.savetxt(file, x, fmt='%.4f', delimiter = ' ' )
        
        file.close()
    
if __name__ == "__main__":
    
    file = open("in1.txt","r")
    n = int(file.readline())
    a = np.zeros([n,n])
    b = np.zeros(n)
        
    for i in range(n):
        line = file.readline()
        num = line.split()
        a[i:] = num[:]
    
    for i in range(n):
        line = file.readline()
        num = line.split()
        b[i:] = num[:]
    
    lu_decomposition(a,b)
    
    

